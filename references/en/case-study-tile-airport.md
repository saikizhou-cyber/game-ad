# Worked Example: Tile Airport X-ray Ad

This is a production case study, not a reusable script template.

## Brief

- Product: overseas Tile matching game.
- Format: vertical performance ad, longer than 10 seconds, English-market visible copy.
- Core proof: click uncovered items, move them into a seven-slot tray, clear three matches, avoid a full tray, clear the board.
- Desired feeling: urgency in the hook, then oddly satisfying/ASMR play and a warm emotional release.
- Production mix: AI narrative footage, AI-generated visual development, deterministic AE gameplay, editor-based sound/music, FFmpeg inspection.

## Final creative spine

1. A warm-toned cartoon raccoon notices its blue suitcase entering an airport X-ray scanner and reacts urgently.
2. The suitcase is shown top-down in a dark enclosed scanner; the scan reveals packed objects.
3. The scan image becomes a vertical top-down AE gameplay board inside the suitcase.
4. The player clicks uncovered travel objects one at a time; items enter a seven-slot tray and clear in threes.
5. Upper objects clear, dim lower objects unlock, and the bag becomes orderly.
6. The suitcase passes inspection; the raccoon jumps happily and leaves for the trip.

## Why it worked

- The X-ray scanner created real urgency without an unrelated device interaction.
- Scanning and revealing hidden objects provided a causal transition into the board.
- The camera moved from an angled character scene to a top-down scan, then preserved top-down geometry in gameplay.
- Warm character colors contrasted with the cool scanner environment.
- The ending completed the original travel goal instead of ending on an abstract clear effect.

## Problems found during production

- A simple paw reaching toward a tile lacked urgency.
- Repeating the same reach immediately before gameplay felt redundant.
- A suitcase-mounted horizontal screen conflicted with a vertical gameplay composition.
- The raccoon could not plausibly press a screen while physically holding the suitcase down.
- “Bag about to burst” was less specific and less causal than an imminent X-ray scan.
- Early versions omitted the suitcase entering the scanner, weakening setup continuity.
- Gameplay arranged pieces as rows instead of overlapping layers.
- Matches were too easy and appeared pre-grouped instead of discovered one tile at a time.
- A moving shell crossed board pieces on its way to the tray.
- Generated background/UI versions drifted from the scanner's art direction.
- Static AI glow images did not provide dynamic gameplay feedback.

## Generalized production lessons

1. Choose a danger that naturally reveals or activates the game mechanic.
2. Design the transition in pre-production; do not attach gameplay after the hook is generated.
3. Let AI handle expressive character and environment invention; let AE handle exact game state, UI, text, and timing.
4. Preserve board coordinates and depth logic; fit the surrounding UI to the gameplay, not the reverse.
5. Review nested AE comps and multiple gameplay states.
6. Use sound to distinguish click, pickup, tray landing, match, unlock, progress, and final release.
7. Return to the original character goal for closure.
8. Validate the final master for watermarks, CTA/logo, safe zones, and true-peak headroom.

## Final review lesson

The self-edited master was visually strong and logically coherent, but publishing review still found common last-mile issues: an AI-generation watermark, missing product logo/CTA, audio reaching 0 dBFS, safe-zone pressure, and a uniform mid-game rhythm. A creative can be successful yet still fail delivery discipline; final QC is part of creative direction, not a separate afterthought.

## Do not copy

Do not automatically reuse the raccoon, suitcase, airport, X-ray machine, scan wipe, exact UI, shot timings, or copy. Transfer only the principles: causal hook, motivated transition, product-truth gameplay, cross-method continuity, and complete payoff.
