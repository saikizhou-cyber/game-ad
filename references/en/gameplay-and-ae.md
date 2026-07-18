# Gameplay, AE, and Compositing Safeguards

## Reconstruct the mechanic before animating

Write the game as states and transitions:

```text
board state -> visible player input -> inventory/state update -> match/fail check -> feedback -> next available input
```

Define legal input, blocking rules, inventory capacity, match threshold, fail condition, and completion condition. Visual polish cannot repair an incoherent state machine.

## Layered Tile-style logic

For a layered Tile mechanic:

- objects overlap spatially; rows alone do not imply depth;
- covered items are blocked, often dimmed, and cannot be selected;
- one uncovered item is found and clicked at a time;
- clicked items move to the tray without crossing unrelated board objects visually;
- three matching tray items clear only after the third arrives;
- a cleared upper layer reveals one or more previously blocked items;
- tray capacity creates readable risk;
- success comes from clearing the board; failure comes from a full tray without a match.

Do not place three identical selectable objects side by side merely to force a match. Build discovery, risk, and release.

## Preserve authoritative coordinates

- Treat designed tile/item coordinates as gameplay truth.
- Never stretch individual board coordinates to fit a new background.
- Fit layout by adjusting the container, UI plate, camera, or precomp transform.
- Preserve aspect ratios and relative overlap unless the mechanic itself changes.
- Audit object paths so a moving tile does not overlap unrelated pieces or UI frames.

## AE project architecture

Prefer reusable precomps:

```text
MASTER_9x16
  STORY_OR_HOOK
  GAMEPLAY
    BG
    BOARD
      DEPTH_BACK
      DEPTH_MID
      DEPTH_FRONT
    INPUT_FX
    TRAY
    PROGRESS
    GAMEPLAY_FX
  ENDING
  COPY_CTA
  AUDIO_GUIDE
```

When inspecting an existing project, traverse nested precomps. Layers may live inside `BG`, `tiles/items`, `tray`, `progress`, or `VFX` rather than the main comp.

## Deterministic animation rules

- Animate one attributable input at a time.
- Use a short anticipation, movement, landing, state update, and payoff cadence.
- Keep click indicators away from moving objects after contact.
- Use protected regions around tray slots, copy, and board edges.
- Let lower layers unlock with scale/light/depth changes, not unexplained teleportation.
- Vary interval and intensity across the sequence: setup, first proof, tension, combo, relief.
- For ASMR, lengthen anticipation and settle, reduce camera noise, and use detailed foley.
- For high-energy ads, compress dead time but retain readable cause/effect frames.

## Effect ownership

Use AI-generated raster effects as design references or texture plates. Build dynamic click, match, scan, progress, and clear effects in AE when timing and repeatability matter.

Separate:

- click ring/input confirmation;
- pickup/motion trail;
- tray landing;
- match/combo burst;
- unlock light;
- progress pulse;
- final clear.

One generic glow applied everywhere weakens feedback hierarchy.

## Review checkpoints

Render and inspect at minimum:

1. first frame;
2. first input;
3. first inventory update;
4. first match;
5. a mid-game blocked/unlocked state;
6. near-fail or peak tension;
7. completion;
8. CTA/end card.

Do not approve layout from a single screenshot.

## Script and desktop-operation policy

- Use ExtendScript for repeatable comp construction, naming, transforms, timing, and batch corrections.
- Use desktop control to verify visual state, render dialogs, and app-only operations when scripting cannot reach them.
- Save versioned AEP files before structural changes.
- Never assume an automation succeeded because the script exited; inspect the resulting frames.
- Preserve user edits and unrelated layers.
