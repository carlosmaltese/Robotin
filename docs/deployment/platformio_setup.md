# PlatformIO Setup

Robotin firmware projects live under `firmware/`.

## Install PlatformIO

Option 1: VS Code PlatformIO extension.

Option 2: Python package:

```bash
python -m pip install platformio
```

Check install:

```bash
pio --version
```

## Firmware Structure

Each subsystem is a separate PlatformIO project:

- `firmware/face_esp32`
- `firmware/head_esp32`
- `firmware/motor_esp32`
- `firmware/lights_esp32`

## Compile

```bash
cd firmware/face_esp32
pio run
```

Repeat from each firmware directory as needed.

## Notes

Current firmware is intentionally skeletal. It initializes serial, prints a ready event and returns `OK` or `ERR unknown command`.

