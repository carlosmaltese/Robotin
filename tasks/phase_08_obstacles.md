# Phase 08: Obstacles

## Objective

Add obstacle sensing and movement inhibition.

## Scope

- Choose sensors.
- Define obstacle events.
- Integrate with safety policy before autonomous movement.

## Checklist

- [ ] Select front sensors.
- [ ] Define minimum stop distance.
- [ ] Add fake obstacle events.
- [ ] Block forward motion on obstacle.

## Acceptance Criteria

- Obstacle state can block movement.
- Tests cover blocked and clear paths.

## Risks

- Sensor blind spots.
- False negatives at low light or bad angles.

## Hardware Notes

Sensor choice is open. Avoid relying on one sensor for all safety.

## Test Commands

```bash
cd raspberry && pytest
python tools/motor_demo.py --fake
```

