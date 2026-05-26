# Phase 07: Movement

## Objective

Add controlled mobile base movement.

## Scope

- Implement motor firmware only after hardware is selected.
- Keep normalized drive commands.
- Enforce safety manager checks on Raspberry.

## Checklist

- [ ] Select motor driver.
- [ ] Define battery and current limits.
- [ ] Add local firmware stop behavior.
- [ ] Test emergency stop.

## Acceptance Criteria

- Emergency stop blocks `MotorAdapter.drive`.
- Motor firmware stops on heartbeat timeout.
- Movement tests use low power and short durations.

## Risks

- Robot moving unexpectedly.
- Inadequate power isolation.

## Hardware Notes

Do not run real motors on USB power.

## Test Commands

```bash
python tools/motor_demo.py --fake
cd raspberry && pytest tests/test_safety_manager.py
```

