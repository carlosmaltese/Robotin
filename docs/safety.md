# Safety

Safety has priority over movement, voice, face and lights.

## Emergency Stop

`SafetyManager` tracks an emergency stop state. When active, movement commands are blocked before they reach the motor adapter.

## Watchdog

The Raspberry should send periodic heartbeat messages:

```text
SYS HEARTBEAT
```

Future motor firmware should stop motors if heartbeat is lost.

## Communication Loss

If a subsystem stops responding:

- motors stop first,
- head motion is disabled,
- face and lights may continue only if safe,
- the orchestrator records the fault.

## Motor Policy

Early motor commands are limited by:

- max normalized power,
- max duration,
- emergency stop state.

Real motor control is intentionally not implemented in this initial repo.

