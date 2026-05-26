# Test Procedures

## Simulation Test

Purpose: verify Python orchestration without hardware.

```bash
cd raspberry
python -m robotin.main --simulation
pytest
```

Run only the simulation boot test:

```bash
cd raspberry
pytest tests/test_simulation_boot.py
```

Alternative from the repository root:

```bash
python tools/run_simulation.py
make test
```

Pass criteria:

- Robotin starts in simulation mode.
- Face, mouth, lights, head and voice mock outputs are printed.
- Tests pass.

Failure hints:

- If the command output changed intentionally, update `test_simulation_boot.py`.
- If config loading fails, verify `robotin/config/robot.yaml` and `robotin/config/devices.yaml`.
- If a serial error appears, simulation mode is accidentally touching hardware code.

## Serial Port Test

Purpose: verify a connected ESP32 appears as a serial device.

```bash
python tools/list_serial_devices.py
python tools/send_command.py --port /dev/ttyUSB0 --line "SYS HEARTBEAT"
```

Pass criteria:

- Port is visible.
- Device responds or monitor shows activity.

## Face Test

Purpose: verify face command path.

```bash
python tools/face_demo.py --simulation
python tools/face_demo.py --port /dev/ttyUSB0 --happy
python tools/face_demo.py --port /dev/ttyUSB0 --sequence basic
```

Pass criteria:

- Fake mode prints commands.
- Level A hardware mode receives `EVT FACE READY`, `OK FACE <COMMAND>` and status events once firmware supports them.
- No GC9A01 graphics are required for Level A.

## Head Test Without Load

Purpose: verify head commands before attaching mechanical load.

```bash
python tools/head_demo.py --fake
python tools/head_demo.py --port /dev/ttyUSB0
```

Pass criteria:

- Commands stay within configured limits.
- No servo is attached until power and limits are verified.

## Motors Test With Wheels in the Air

Purpose: verify motor command path safely.

```bash
python tools/motor_demo.py --fake
python tools/motor_demo.py --port /dev/ttyUSB0
```

Pass criteria:

- Wheels do not touch the ground.
- E-STOP is reachable.
- Stop command works.

## Lights Test

Purpose: verify lights command path.

```bash
python tools/send_command.py --line "LIGHT MODE warm"
python tools/send_command.py --port /dev/ttyUSB0 --line "LIGHT MODE warm"
```

Pass criteria:

- Fake serial prints the command.
- Hardware mode returns `OK` once firmware is flashed.

## Heartbeat Test

Purpose: verify subsystem heartbeat command.

```bash
python tools/send_command.py --port /dev/ttyUSB0 --line "SYS HEARTBEAT"
```

Pass criteria:

- Subsystem returns `OK`.
- Future motor firmware stops on heartbeat timeout.

## Emergency Stop Test

Purpose: verify movement blocking.

```bash
cd raspberry
pytest tests/test_safety_manager.py
```

Pass criteria:

- Emergency stop blocks motor drive.
- Stop command remains available.
