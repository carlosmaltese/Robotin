# Development

## Python

```bash
cd raspberry
python -m pip install -e .[dev]
pytest
python -m robotin.main --simulation
```

Use simulation mode until a subsystem has been tested independently.

## PlatformIO

Each firmware folder is a separate PlatformIO project:

```bash
cd firmware/face_esp32
pio run
```

Board targets are placeholders for ESP32-WROOM class boards and can be changed per hardware revision.

## Serial Debugging

List ports:

```bash
python tools/list_serial_devices.py
```

Send a command:

```bash
python tools/send_command.py --port COM3 --line "SYS HEARTBEAT"
```

Monitor logs:

```bash
python tools/monitor_subsystem.py --port COM3
```

