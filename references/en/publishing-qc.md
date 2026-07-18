# Publishing and Final-Ad QC

## Visual editorial review

Inspect the full ad and contact sheets for:

- first-frame comprehension;
- hook escalation through 3 seconds;
- clean transition into product proof;
- midsection rhythm and new information;
- climax/payoff strength;
- logo, CTA, and end-card duration;
- accidental watermarks, generation marks, placeholder text, or brand conflicts;
- anatomy, prop continuity, UI drift, collision, cropping, and letterboxing;
- mobile readability and platform safe zones.

For 9:16 ads, keep critical copy, tray, CTA, and interaction away from platform overlay regions. Validate against the current platform delivery guide when exact safe zones matter.

## Audio review

Confirm:

- an audio stream exists;
- hook transient is audible but not clipped;
- clicks/foley align to visible contacts;
- mechanic feedback has hierarchy;
- BGM arc supports tension and payoff;
- dialogue/VO remains intelligible;
- no abrupt ambience cut at method transitions;
- true peak has headroom and export does not hit 0 dBFS;
- perceived loudness is appropriate for the placement.

Use a final limiter ceiling around -1 dBTP unless the delivery specification says otherwise. Do not treat this as a substitute for a balanced mix.

## Technical checklist

- expected duration and no accidental handles;
- correct aspect ratio and resolution;
- stable frame rate;
- supported codec/profile/pixel format;
- audio codec, sample rate, and channel layout;
- no missing frames or black gaps;
- no incorrect color shift or crushed shadows;
- filename/version matches the approved master;
- source project and dependencies are archived when required.

## Contact-sheet sampling

Sample:

- 0.0s;
- 0.5s;
- 1.5s;
- 3.0s;
- transition midpoint;
- first product input;
- mid-game;
- pre-payoff;
- payoff;
- CTA/end frame.

For long ads, add regular interval samples. Contact sheets reveal pacing and visual repetition, but still watch the full render with audio.

## Publishing decision

Classify findings:

- **Blocker**: broken logic, missing product proof, unreadable format, clipping, watermark, missing CTA/logo when required, corrupted render.
- **High priority**: weak first three seconds, causality gap, major continuity error, unsafe copy placement, uniform middle rhythm.
- **Polish**: micro-timing, secondary effect, color nuance, optional copy refinement.

Deliver a ranked repair list with exact timecodes and the expected performance impact.

## Variant readiness

Before calling a master scalable, confirm these can change independently:

- first-frame hook;
- opening copy;
- gameplay difficulty/state;
- pacing profile;
- payoff/end reaction;
- CTA text;
- locale and platform safe zones.
