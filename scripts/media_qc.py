#!/usr/bin/env python3
"""Inspect a finished ad with ffprobe/ffmpeg and emit a reproducible QC report."""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path


def executable(name: str, override: str | None) -> str:
    if override:
        path = Path(override)
        if path.exists():
            return str(path)
        raise FileNotFoundError(f"{name} override does not exist: {override}")
    found = shutil.which(name)
    if not found:
        raise FileNotFoundError(f"{name} was not found. Install FFmpeg or pass --{name}-path.")
    return found


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True, check=False)


def parse_ratio(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"\s*(\d+)\s*[:/]\s*(\d+)\s*", value)
    if not match:
        raise argparse.ArgumentTypeError("aspect must look like 9:16 or 16/9")
    a, b = int(match.group(1)), int(match.group(2))
    if a <= 0 or b <= 0:
        raise argparse.ArgumentTypeError("aspect terms must be positive")
    return a, b


def probe(ffprobe: str, media: Path) -> dict:
    result = run([
        ffprobe, "-v", "error", "-show_entries",
        "format=duration,format_name,bit_rate:stream=index,codec_type,codec_name,profile,width,height,pix_fmt,r_frame_rate,avg_frame_rate,sample_rate,channels,channel_layout",
        "-of", "json", str(media),
    ])
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "ffprobe failed")
    return json.loads(result.stdout)


def audio_stats(ffmpeg: str, media: Path) -> dict:
    peak = run([
        ffmpeg, "-hide_banner", "-nostats", "-i", str(media), "-map", "0:a:0",
        "-af", "volumedetect", "-f", "null", "-",
    ])
    combined = peak.stderr + "\n" + peak.stdout
    mean_match = re.search(r"mean_volume:\s*([-+\d.]+)\s*dB", combined)
    max_match = re.search(r"max_volume:\s*([-+\d.]+)\s*dB", combined)

    loudness = run([
        ffmpeg, "-hide_banner", "-nostats", "-i", str(media), "-map", "0:a:0",
        "-af", "ebur128=peak=true", "-f", "null", "-",
    ])
    ltext = loudness.stderr + "\n" + loudness.stdout
    integrated = re.findall(r"I:\s*([-+\d.]+)\s*LUFS", ltext)
    true_peak = re.findall(r"Peak:\s*([-+\d.]+)\s*dBFS", ltext)
    return {
        "mean_volume_db": float(mean_match.group(1)) if mean_match else None,
        "max_volume_db": float(max_match.group(1)) if max_match else None,
        "integrated_lufs": float(integrated[-1]) if integrated else None,
        "true_peak_dbfs": float(true_peak[-1]) if true_peak else None,
    }


def make_contact_sheet(
    ffmpeg: str, media: Path, output: Path, samples: int, duration: float
) -> None:
    columns = 3
    rows = math.ceil(samples / columns)
    output.parent.mkdir(parents=True, exist_ok=True)
    interval = max(duration / samples, 0.05)
    vf = f"fps=1/{interval:.6f},scale=360:-2,tile={columns}x{rows}"
    result = run([
        ffmpeg, "-y", "-hide_banner", "-i", str(media), "-vf", vf,
        "-frames:v", "1", str(output),
    ])
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "contact sheet generation failed")


def build_report(data: dict, args: argparse.Namespace, audio: dict | None) -> dict:
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)
    duration = float(data.get("format", {}).get("duration") or 0.0)
    checks: list[dict] = []

    def add(name: str, passed: bool, actual, expected) -> None:
        checks.append({"name": name, "pass": bool(passed), "actual": actual, "expected": expected})

    add("duration", duration >= args.min_duration, round(duration, 3), f">= {args.min_duration}s")
    add("video_stream", video is not None, bool(video), True)
    add("audio_stream", audio_stream is not None, bool(audio_stream), True)

    if video:
        width, height = int(video.get("width") or 0), int(video.get("height") or 0)
        expected_w, expected_h = args.expect_aspect
        actual_ratio = width / height if height else 0
        expected_ratio = expected_w / expected_h
        add(
            "aspect_ratio",
            abs(actual_ratio - expected_ratio) <= args.aspect_tolerance,
            f"{width}:{height}", f"{expected_w}:{expected_h}",
        )
        add(
            "minimum_resolution",
            width >= args.min_width and height >= args.min_height,
            f"{width}x{height}", f">= {args.min_width}x{args.min_height}",
        )

    if audio:
        max_db = audio.get("max_volume_db")
        true_peak = audio.get("true_peak_dbfs")
        measured_peak = true_peak if true_peak is not None else max_db
        add(
            "audio_peak_headroom",
            measured_peak is not None and measured_peak <= args.max_peak,
            measured_peak, f"<= {args.max_peak} dB",
        )

    return {
        "file": str(args.media.resolve()),
        "summary": {
            "duration_seconds": round(duration, 3),
            "format": data.get("format", {}).get("format_name"),
            "video": video,
            "audio": audio_stream,
            "audio_measurements": audio,
        },
        "checks": checks,
        "pass": all(item["pass"] for item in checks),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("media", type=Path)
    parser.add_argument("--min-duration", type=float, default=10.0)
    parser.add_argument("--expect-aspect", type=parse_ratio, default=(9, 16))
    parser.add_argument("--aspect-tolerance", type=float, default=0.01)
    parser.add_argument("--min-width", type=int, default=1080)
    parser.add_argument("--min-height", type=int, default=1920)
    parser.add_argument("--max-peak", type=float, default=-1.0)
    parser.add_argument("--skip-audio-analysis", action="store_true")
    parser.add_argument("--contact-sheet", type=Path)
    parser.add_argument("--contact-samples", type=int, default=12)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--ffmpeg-path")
    parser.add_argument("--ffprobe-path")
    args = parser.parse_args()

    if not args.media.is_file():
        parser.error(f"media does not exist: {args.media}")

    try:
        ffprobe = executable("ffprobe", args.ffprobe_path)
        ffmpeg = None
        if not args.skip_audio_analysis or args.contact_sheet:
            ffmpeg = executable("ffmpeg", args.ffmpeg_path)
        data = probe(ffprobe, args.media)
        has_audio = any(s.get("codec_type") == "audio" for s in data.get("streams", []))
        audio = audio_stats(ffmpeg, args.media) if ffmpeg and has_audio and not args.skip_audio_analysis else None
        if args.contact_sheet and ffmpeg:
            duration = float(data.get("format", {}).get("duration") or 0.0)
            make_contact_sheet(
                ffmpeg, args.media, args.contact_sheet,
                max(3, args.contact_samples), duration,
            )
        report = build_report(data, args, audio)
    except (FileNotFoundError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
