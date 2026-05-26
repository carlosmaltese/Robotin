# Phase 03: AI Expressions

## Objective

Map AI intentions to face, head, lights and voice mock actions.

## Scope

- Keep AI output at intention level.
- Route emotion, gaze, head gesture, lights and utterance.
- Avoid direct physical commands from AI.

## Checklist

- [ ] Extend intent schema if needed.
- [ ] Add more mock intents.
- [ ] Add router tests.
- [ ] Keep safety checks outside AI.

## Acceptance Criteria

- `python -m robotin.main --simulation` prints the full mock flow.
- Router tests verify adapter calls.

## Risks

- Letting AI bypass safety and adapters.
- Growing intent schema too early.

## Hardware Notes

No hardware required.

## Test Commands

```bash
cd raspberry && python -m robotin.main --simulation
cd raspberry && pytest tests/test_intent_router.py
```

