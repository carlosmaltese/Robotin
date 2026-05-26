# Phase 05: Head Servos

## Objective

Add safe pan/tilt head movement.

## Scope

- Define mechanical limits.
- Add servo controller implementation.
- Keep gestures mapped by Raspberry, not AI direct commands.

## Checklist

- [ ] Select servos.
- [ ] Define pan/tilt ranges.
- [ ] Add external power supply.
- [ ] Test `HEAD LOOK` and `HEAD GESTURE`.

## Acceptance Criteria

- Head firmware acknowledges known commands.
- Software limits match measured mechanical limits.
- Center command is safe.

## Risks

- Servo stall current.
- Mechanical collision at extreme angles.

## Hardware Notes

Use common ground and external servo power.

## Test Commands

```bash
python tools/head_demo.py --fake
python tools/send_command.py --port COM3 --line "HEAD LOOK 15 -5"
```

