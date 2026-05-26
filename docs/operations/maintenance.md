# Maintenance

## Cable Review

- Inspect cables before movement tests.
- Look for loose Dupont wires.
- Replace damaged insulation.
- Confirm labels are still readable.

## Connector Review

- Check that connectors are fully seated.
- Prefer locking connectors for moving parts.
- Avoid unsupported hanging cables.
- Recheck polarity before reconnecting power.

## Configuration Backup

Back up:

- `raspberry/robotin/config/robot.yaml`
- `raspberry/robotin/config/devices.yaml`
- future udev rules,
- hardware change notes.

## Firmware Updates

Before flashing:

- disconnect motor power,
- stop serial monitors,
- confirm correct PlatformIO project,
- record firmware change in hardware log.

After flashing:

- confirm ready event,
- run subsystem smoke test,
- update notes if pinout or behavior changed.

## Hardware Change Log

Record:

- date,
- subsystem,
- wiring change,
- firmware version or commit,
- test command used,
- result,
- follow-up TODOs.

