# Robotin

Robotin is a modular domestic robot project. The Raspberry Pi is the central brain and ESP32 boards act as specialized controllers for face, head, motors and lights.

The repository starts with a practical simulation-first architecture. It does not implement real AI, vision, motor control or display drivers yet. The first goal is a clean base that can be debugged on a development machine before hardware is connected.

## Architecture

- Raspberry Pi 4B now, Raspberry Pi 5 + AI HAT later.
- ESP32 subsystems connected by USB serial for internal control.
- Initial protocol: plain text commands, one line per command.
- Future protocol: JSON Lines when messages need richer payloads.
- Python adapters isolate each subsystem from orchestration logic.
- Fake adapters allow development without hardware.
- AI produces high-level intentions only. The Raspberry translates intentions into physical commands.
- Safety logic lives in `raspberry/robotin/safety`, not only in the orchestrator.

## Documentation

- [Architecture](docs/architecture.md)
- [Protocol](docs/protocol.md)
- [Hardware overview](docs/hardware/overview.md)
- [Hardware bill of materials](docs/hardware/bill_of_materials.md)
- [Power architecture](docs/hardware/power_architecture.md)
- [Wiring conventions](docs/hardware/wiring_conventions.md)
- [Deployment guide](docs/deployment/raspberry_setup.md)
- [Python environment](docs/deployment/python_environment.md)
- [PlatformIO setup](docs/deployment/platformio_setup.md)
- [Firmware flashing](docs/deployment/flashing_firmware.md)
- [Serial devices](docs/deployment/serial_devices.md)
- [Operations startup and shutdown](docs/operations/startup_shutdown.md)
- [Safety checklist](docs/operations/safety_checklist.md)
- [Test procedures](docs/operations/test_procedures.md)
- [Maintenance](docs/operations/maintenance.md)
- [Roadmap](docs/roadmap.md)

## Project Phases

1. Face eyes with ESP32 and GC9A01 displays.
2. Raspberry to ESP32 serial protocol.
3. AI-driven expressions and voice mock flow.
4. TFT mouth subsystem.
5. Head pan/tilt servos.
6. Vision service.
7. Mobile base movement.
8. Obstacle sensors and movement safety.

Suggested GitHub issues are listed in [docs/roadmap.md](docs/roadmap.md).

## Install Python Dependencies

```bash
cd raspberry
python -m pip install -e ".[dev]"
```

For real serial hardware later:

```bash
python -m pip install -e ".[dev,serial]"
```

## Run Simulation

From the Raspberry package directory:

```bash
cd raspberry
python -m robotin.main --simulation
```

From the repository root:

```bash
python tools/run_simulation.py
```

Expected output:

```text
[robotin] starting in simulation mode
[robotin] loading configuration
[robotin] orchestrator started
[face] FACE EXPR happy
[face] FACE LOOK center
[face] FACE MOUTH talking
[light] LIGHT MODE warm
[head] HEAD GESTURE small_nod
[voice] Hola, soy Robotin.
[robotin] demo completed
```

## Send a Test Command

Fake mode:

```bash
python tools/face_demo.py --fake
```

Serial mode:

```bash
python tools/send_command.py --port COM3 --line "FACE EXPR happy"
```

## Run Tests

```bash
cd raspberry
pytest
```

Run one test file:

```bash
cd raspberry
pytest tests/test_simulation_boot.py
```

Or from the repository root:

```bash
make test
```

Basic failure reading:

- Parser failures usually point to `robotin/protocol/parser.py` or command builders.
- Simulation boot failures usually mean startup output, config loading or fake adapter routing changed.
- Safety failures must be reviewed before any future motor hardware work.
