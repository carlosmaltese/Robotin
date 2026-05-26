# Phase 06: Vision

## Objective

Introduce a vision service on the Raspberry.

## Scope

- Keep a mock camera service first.
- Add real camera later.
- Emit high-level observations, not direct actions.

## Checklist

- [ ] Define observation event shape.
- [ ] Add camera config.
- [ ] Add mock frame tests.
- [ ] Decide real camera library.

## Acceptance Criteria

- Vision can run disabled or mocked.
- Orchestrator can subscribe to observation events.

## Risks

- CPU load on Raspberry Pi 4B.
- Tight coupling between vision and movement.

## Hardware Notes

Camera hardware is not required for this initial phase.

## Test Commands

```bash
cd raspberry && pytest
```

