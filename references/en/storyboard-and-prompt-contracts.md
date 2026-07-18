# Storyboard and Prompt Contracts

## Production storyboard schema

Every shot must include:

- exact in/out time;
- viewer job: attract, clarify, intensify, prove, reward, or convert;
- composition, subject, action, and visible state change;
- camera and transition;
- copy/dialogue exactly as shown or spoken;
- SFX, ambience, BGM emotion, and VO;
- production method and source assets;
- exit frame needed by the next shot;
- acceptance test.

Avoid describing an entire sequence as one “shot” when it contains multiple spatial or causal changes.

## Image-generation prompt contract

Map each prompt to an explicit storyboard location:

```text
Asset ID: <shot number + asset role>
Storyboard use: <exact shot/time>
Use case: <concept frame/UI/background/prop/character/keyframe>
Primary request: <one visible outcome>
References: <image index and role for each input>
Scene/backdrop: <location and depth>
Subject/action: <who/what, pose, state>
Style/medium: <photo, stylized 3D, illustration, UI plate>
Composition/camera: <aspect, shot size, angle, lens, screen position>
Lighting/mood: <direction, temperature, contrast>
Palette/material: <specific anchors>
Continuity invariants: <must remain unchanged>
Text: <prefer none; otherwise exact quoted copy>
Avoid: <defects, extra objects, watermark, cropped limbs, duplicate props>
```

Generate independent assets independently. Do not ask one image to serve incompatible camera angles or states.

## First/last-frame video contract

For every generated video group, define:

```text
Video group: <ID, duration>
Storyboard use: <shots/time range>
Start-frame reference: <asset ID and required invariants>
End-frame reference: <asset ID and required invariants>
Character/prop lock: <appearance, placement, ownership>
Environment lock: <layout, light, weather, signage>
Motion beats:
  [0.0-1.2s] <action + camera + sound source>
  [1.2-2.8s] <action + camera + sound source>
  [2.8-4.0s] <exit pose + edit handoff>
Continuity: <screen direction, eyeline, object path>
Negative constraints: <no morphing, extra limbs, prop duplication, text, watermark>
```

Use the smallest set of reference images that fully establishes the group. More references are not automatically better; conflicting references weaken control.

## All-reference generation

When a model supports “all reference” inputs:

1. Number uploaded frames in chronological order.
2. State the role of every reference: identity, scene, start state, end state, prop, or style.
3. Tell the model which differences are intentional.
4. Remove redundant frames that do not add identity or motion information.
5. Keep one continuous action objective per generated clip.
6. Add no exact UI/text unless the model is only producing a background plate.

## AI-to-deterministic handoff

Use one or more anchors:

- object silhouette match;
- camera push through a device/surface;
- scanning line or light wipe;
- motion-direction match;
- color flash with preserved subject position;
- sound pre-lap into the mechanic;
- identical top-down geometry.

The transition must preserve meaning, not only appearance. A scanner can reveal hidden gameplay because scanning and revealing are causally related; an unrelated button cannot.

## Prompt QA

Before generation, verify:

- every prompt names its storyboard use;
- camera direction and aspect ratio are explicit;
- start/end states are compatible;
- only one complex body action is requested at a time;
- important props have one owner and one path;
- visible text is removed from AI responsibility;
- the exit frame can be edited into the next shot;
- there is a cheaper fallback for the hardest generation.
