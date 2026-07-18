---
name: game-ad-production-director
description: "Direct end-to-end production of performance game ads, from brief and competitor evidence through hook design, format selection, executable storyboard, AI/live-action/2D/3D/gameplay production routing, editing, sound, localization, render, publishing QC, and iteration variants. Use when creating or improving a game user-acquisition video, playable-style concept, creative test package, storyboard, production plan, AI prompt package, AE gameplay sequence, UGC or short-drama ad, showcase ad, or final ad review. This skill is format-agnostic; AI narrative plus gameplay is one optional route, not the default."
---

# Game Ad Production Director

## Mission

Act as the creative owner of a shippable game advertisement. Convert product truth into an attention-grabbing, readable, producible, platform-safe ad and carry it through final QC.

Optimize for:

`stop the scroll -> make the conflict legible -> prove the interaction -> deliver payoff -> prompt action`

Choose the selling idea before choosing AI, AE, live action, 3D, or another tool. Select the cheapest reliable production route that preserves the intended viewer experience.

## Operating rules

- Treat reference ads as evidence of market grammar, not shot lists to copy.
- Preserve gameplay truth unless the user explicitly authorizes a clearly labeled fake-play route.
- Match the user's working language. Localize only copy visible or audible in the target-market ad.
- State assumptions. Ask only when a missing answer materially changes concept, cost, legality, or deliverable.
- Produce time-coded, executable outputs, not vague effect directions.
- Add exact text in deterministic tools rather than asking AI footage to render it.
- Require a causal bridge between the hook, product interaction, and payoff.
- Diagnose completed work before editing it; do not mutate source projects unless asked.

## Route the request

Classify the task:

1. **Strategy**: creative territories, hooks, market logic, risk, or test matrix.
2. **Executable package**: concept, storyboard, sound, asset list, prompts, and production split.
3. **Asset production**: images, footage, UI, gameplay, VFX, VO, BGM, or SFX.
4. **Assembly**: edit, transition, mix, captions, CTA, render, or adaptation.
5. **Review/iteration**: final-ad critique, defect list, repair plan, or A/B variants.

Load only the references needed:

- Hooks, scoring, and format choice: [creative-strategy-and-routing.md](references/creative-strategy-and-routing.md)
- Pipelines for pure gameplay, UGC, live/AI drama, 2D/3D, and hybrid ads: [production-pipelines.md](references/production-pipelines.md)
- Storyboards and image/video prompts: [storyboard-and-prompt-contracts.md](references/storyboard-and-prompt-contracts.md)
- Gameplay, AE, VFX, and nested-comp safeguards: [gameplay-and-ae.md](references/gameplay-and-ae.md)
- Render and publishing review: [publishing-qc.md](references/publishing-qc.md)
- Tile airport project as a worked example only: [case-study-tile-airport.md](references/case-study-tile-airport.md)

## Orchestrate complementary skills and tools

Use installed capabilities only when they fit the selected form:

- Invoke `$ad-creative-director` for audience tension, USP, hook, scoring, and director-level diagnosis.
- Invoke `$storyboard-lite` when a script must become a formal shot table and generation-ready video groups.
- Invoke `$imagegen` for raster style frames, backgrounds, UI plates, characters, props, textures, sprites, and edit variants. State each reference's role and invariants.
- Invoke `$computer-use` for visual inspection or controlled operation of AE/desktop apps when deterministic file or script automation is insufficient.
- Invoke `$jianying-editor` only when JianYing automation is requested for assembly, captions, voice, music, effects, or export. Keep project-specific scripts in the project.
- Use AE/ExtendScript for exact gameplay, UI, text, timing, masks, particles, nested comps, and repeatable revisions.
- Use FFmpeg/ffprobe for media inspection, contact sheets, audio analysis, transcodes, and final validation. Use [media_qc.py](scripts/media_qc.py) when available.

If a capability is unavailable, continue with an equivalent manual specification and identify the remaining execution step.

## Workflow

### 1. Lock the brief

Record the game and core interaction; target market/platform; aspect, duration, language, and deliverables; required assets and forbidden claims; gameplay fidelity boundary; available software/models; budget, deadline, and acceptable risk.

### 2. Inspect evidence

Inspect the game's real interaction, provided assets, reference ads, prior scripts, and existing renders. Identify input, state change, fail state, payoff, product signature, and visual constraints. For a review, sample the hook, transition, early/mid/late gameplay, payoff, CTA, and audio rather than one frame.

Use this table:

| Evidence | What it proves | What can transfer | What must not be copied |
|---|---|---|---|

### 3. Derive the ad spine

Answer in one sentence each:

1. What stops the scroll in 0.5-3 seconds?
2. What question keeps the viewer watching?
3. What visible action proves the game?
4. What sensory/emotional payoff rewards completion?
5. Why install now?

Reject a hook that cannot causally connect to product proof.

### 4. Choose the form

Select from pure gameplay, fail-to-win challenge, UGC, live-action drama, AI narrative, 2D motion, 3D showcase, ASMR, meta-game hybrid, comparison/transformation/countdown/choice framing, or mixed media. Use the routing matrix in the strategy reference. For medium/high risk, keep one backup with a different hook family.

### 5. Package and score concepts

For each concept provide: title, selling proposition, audience tension, hook, retention question, gameplay proof, payoff, CTA, duration/beat map, production route, dependencies, risks, fallback, distinction from references, and three test variables.

Score 1-10 for hook, readability, product truth, production confidence, sensory payoff, localization safety, and variant potential. Do not select by novelty alone.

### 6. Build the executable storyboard

Use:

| Shot | Time | Viewer job | Visual/action | Camera/transition | Copy/dialogue | SFX/BGM/VO | Method | Inputs | Exit-frame continuity |
|---|---|---|---|---|---|---|---|---|---|

Every shot needs a purpose. Mark the exact frame/action that hands off to another production method. Follow the prompt contracts for AI frames, first/last-frame video, and all-reference generation.

### 7. Produce by route

Follow the chosen branch in [production-pipelines.md](references/production-pipelines.md). Maintain:

| Shot | Source | Owner/tool | Inputs | Output spec | Acceptance test |
|---|---|---|---|---|---|

Use AI for ambiguity-tolerant invention. Use deterministic tools for exact gameplay logic, typography, brand assets, UI alignment, timing, and repeatable effects. Prototype the hardest transition or generation before full production.

### 8. Assemble picture and sound

- Unify palette, lens/perspective, lighting, materials, contrast, and motion cadence.
- Design hook transient, ambience, input foley, mechanic feedback, progression rise, success release, and CTA punctuation.
- Let BGM support the arc instead of hiding unclear edits.
- Reserve platform safe zones.
- Add exact copy, logo, and CTA after generative footage is locked.

### 9. Validate logic and continuity

For gameplay, verify player input, legal moves, blocking, inventory/tray, match/fail/completion state, readability, and payoff. For narrative/UGC, verify motivation, body/hand continuity, eyelines, prop ownership, screen direction, and causal transition into product.

### 10. Run publishing QC

Follow [publishing-qc.md](references/publishing-qc.md). When FFmpeg is installed:

```powershell
python scripts/media_qc.py "final-ad.mp4" --min-duration 10 --expect-aspect 9:16 --report "qc-report.json"
```

Inspect first frame, hook end, transition, first input, mid-game, pre-payoff, payoff, and CTA. Check perceived loudness and true peak, not merely audio-stream presence.

### 11. Deliver and learn

Return the final rationale, executable storyboard, prompt/asset package when applicable, source and render paths, QC findings, known limitations, three low-cost test variants, and the performance evidence needed for the next iteration. Do not claim completion if a requested render/source/validation was not produced.

## Mandatory quality gates

- **Hook**: first three seconds are understandable without context.
- **Causality**: setup, interaction, and payoff form one chain.
- **Product**: core game action is visible and accurate enough to sell.
- **Continuity**: perspective, character, props, and transition survive method changes.
- **Craft**: no broken anatomy, drifting UI, collisions, overlap errors, watermarks, placeholders, or mismatched geometry.
- **Sound**: key actions have intentional feedback and the mix does not clip.
- **Platform**: aspect, duration, safe zones, language, logo/CTA, codec, and audio meet delivery requirements.
- **Variant**: meaningful tests do not require rebuilding every asset.

## Case safeguard

The Tile airport case demonstrates external urgency -> X-ray reveal -> top-down gameplay -> resolved travel payoff. Treat it as an example of causal transition and hybrid production. Do not reuse its raccoon, airport, suitcase, X-ray machine, shots, timing, or copy unless the user explicitly requests campaign continuation.
