# Phase 04: TFT Mouth

## Objective

Add a future rectangular TFT mouth subsystem.

## Scope

- Choose display.
- Define commands for mouth states.
- Keep rendering separate from expression routing.

## Checklist

- [ ] Select display module.
- [ ] Add wiring document.
- [ ] Define `FACE MOUTH` command family.
- [ ] Add fake mouth behavior.

## Acceptance Criteria

- Mouth commands are documented and simulated.
- No real graphics driver is required in this phase.

## Risks

- SPI bus contention with eye displays.
- Power budget underestimation.

## Hardware Notes

Check whether mouth display shares the face ESP32 or needs a dedicated controller.

## Test Commands

```bash
cd raspberry && pytest
python tools/face_demo.py --fake
```

