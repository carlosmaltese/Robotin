# Phase 00: Foundation Hardware Docs

## Objective

Create the base hardware, deployment and operations documentation for Robotin before deeper hardware implementation begins.

## Scope

- Hardware architecture overview.
- Initial BOM.
- Power architecture.
- Wiring conventions.
- Raspberry and ESP32 pinout placeholders.
- Logical connector definitions.
- Raspberry setup and Python environment.
- PlatformIO and firmware flashing notes.
- Serial device documentation.
- Startup, shutdown, safety and maintenance procedures.

## Checklist

- [ ] Hardware overview exists.
- [ ] BOM exists with available, recommended, future and avoid sections.
- [ ] Power architecture includes separate Raspberry, servo and motor power guidance.
- [ ] Wiring conventions exist.
- [ ] Pinout docs exist for Raspberry, face ESP32, head ESP32, motor ESP32 and lights ESP32.
- [ ] Connector docs define FACE, HEAD, MOTOR, LIGHT, ESTOP and POWER_DISTRIBUTION.
- [ ] Deployment docs cover Raspberry setup, Python, PlatformIO, flashing, serial devices, logs and troubleshooting.
- [ ] Operations docs cover startup/shutdown, safety checklist, test procedures and maintenance.
- [ ] README links architecture, protocol, hardware, deployment, operations and roadmap.
- [ ] Critical undecided hardware choices are marked with TODO.

## Acceptance Criteria

- [ ] Base hardware documentation exists.
- [ ] Base deployment documentation exists.
- [ ] Base operations documentation exists.
- [ ] README links all major documentation areas.
- [ ] No critical decision is hidden without a visible TODO.

## Risks

- Pinouts may be copied into hardware before validation.
- Power requirements may be underestimated until real current is measured.
- Documentation can drift if wiring changes are not recorded.

## Test Commands

```bash
cd raspberry
python -m robotin.main --simulation
pytest
```

```bash
python tools/list_serial_devices.py
```
