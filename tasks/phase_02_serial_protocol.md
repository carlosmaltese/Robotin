# Phase 02: Raspberry to ESP32 Serial Protocol

## Objective

Stabilize the line-based serial protocol between Raspberry and ESP32 subsystems.

## Scope

- Keep commands human-readable.
- Add acknowledgement behavior.
- Document event messages.

## Checklist

- [ ] Validate parser for all initial commands.
- [ ] Test heartbeat.
- [ ] Test command timeout behavior.
- [ ] Document transition path to JSON Lines.

## Acceptance Criteria

- Parser tests pass.
- Each subsystem recognizes `SYS HEARTBEAT`.
- Manual serial tools can send and monitor commands.

## Risks

- Ambiguous commands as payloads grow.
- Missing timeout handling on early firmware.

## Hardware Notes

Use USB serial only for internal control.

## Test Commands

```bash
cd raspberry && pytest tests/test_protocol_parser.py
python tools/send_command.py --port COM3 --line "SYS HEARTBEAT"
```

