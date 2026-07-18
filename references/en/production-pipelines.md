# Production Pipelines by Creative Form

## Common pre-production package

Before selecting a branch, lock:

- target platform and delivery spec;
- core interaction and legal fail/win state;
- chosen hook and payoff;
- visual bible: palette, material, camera, contrast, character rules, UI rules;
- audio arc and key event list;
- shot ownership and handoff frames;
- version naming and folder structure.

Suggested project structure:

```text
project/
  00_brief/
  01_references/
  02_storyboard/
  03_ai_art/
  04_ai_video/
  05_gameplay/
  06_audio/
  07_edit/
  08_renders/
  09_qc/
```

## A. Pure gameplay / AE motion-design ad

Use when the core loop itself can stop the scroll.

1. Reconstruct the actual game rule and state machine.
2. Design the first frame as a puzzle or imminent failure, not a neutral board.
3. Block board, input, inventory, progression, fail, and success states.
4. Animate readable player clicks one by one.
5. Use sound and micro-motion to make state changes tactile.
6. Vary tension and payoff across the middle; do not repeat equal-length clicks mechanically.
7. Add CTA/logo only after gameplay readability is locked.

Best for: puzzle, sorting, Tile, merge, idle upgrade, shooter power curves, makeover progression.

## B. UGC / creator-native ad

Use when social proof or personality can sell the interaction.

1. Write spoken copy as a human reaction, not corporate narration.
2. Show product proof early enough to validate the claim.
3. Keep jump cuts, captions, and framing native to the platform.
4. Give the creator a concrete behavior: attempt, mistake, surprise, correction, recommendation.
5. Prepare clean gameplay inserts and a caption-safe edit.

Avoid: long monologues before product, fake phone handling that does not match screen action, and overproduced lighting that defeats the UGC premise.

## C. Live-action or AI short drama

Use only when the character problem creates a causal reason to play.

1. Establish goal, obstacle, and ticking clock visually.
2. Make the character's action physically plausible.
3. Design a bridge object, camera move, match cut, scan, wipe, portal, or screen transition into the product.
4. Ensure the game action resolves or reframes the story problem.
5. Return to the character for emotional closure when it increases payoff.

For AI video:

- minimize simultaneous hand/object/face complexity;
- use reference frames to lock character, props, layout, and lighting;
- split hard actions into shots rather than demanding one impossible continuous motion;
- generate clean footage without exact copy; add typography later;
- define exit pose and entry pose for every edit.

## D. AI visual showcase / metaphor

Use when impossible transformation or world-building is the hook.

1. Map every visual metaphor to an actual product feature.
2. Build a small number of hero images with consistent art direction.
3. Animate with controlled camera, material transformation, and object hierarchy.
4. Insert deterministic UI/gameplay proof before the viewer mistakes the ad for an unrelated film.
5. Keep the final product identity unmistakable.

## E. 2D/3D product showcase

Use when visual polish, object behavior, or progression is the main sell.

1. Storyboard silhouettes and value contrast before detailed modeling.
2. Use a clear cause/effect animation grammar.
3. Reserve close-ups for mechanics and wide shots for scale/payoff.
4. Build reusable rigs, materials, cameras, and effect presets for variants.
5. Composite brand/UI text deterministically.

## F. Hybrid production

Use when no single medium can deliver both hook and proof.

Define a handoff contract for each boundary:

| Property | Outgoing shot | Incoming shot |
|---|---|---|
| framing/aspect | exact crop and subject size | matching entry composition |
| perspective | lens/angle/horizon | equivalent or motivated change |
| palette | dominant hue and luminance | carried accent or deliberate contrast |
| motion | direction, speed, blur | continuation or impact cut |
| object | silhouette and screen location | same anchor or explained transform |
| sound | pre-lap, hit, or suction | continuation and new ambience |

Prototype the hardest boundary first.

## Sound pipeline

Build sound in layers:

1. **Hook transient**: alarm, impact, gasp, snap, or high-contrast silence.
2. **World bed**: room tone, crowd, machine hum, wind, or device ambience.
3. **Input foley**: tap, drag, pickup, drop, swipe.
4. **Mechanic feedback**: lock, unlock, match, combo, fail, progress.
5. **Payoff release**: burst, chime, open space, character reaction.
6. **BGM arc**: tension -> motion -> lift -> CTA punctuation.

Do not solve unclear picture editing by making the mix louder.

## Version strategy

Separate creative variables:

- V1/V2: different hook family;
- A/B: same hook with different first action or copy;
- pacing variants: fast proof vs ASMR release;
- payoff variants: character closure vs gameplay completion;
- CTA variants: challenge, benefit, or direct install.

Change one major variable per test when attribution matters.
