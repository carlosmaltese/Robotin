# Flashing Firmware

Use PlatformIO from each subsystem directory.

## Face ESP32

```bash
cd firmware/face_esp32
pio run
pio run --target upload
pio device monitor
```

Expected ready line:

```text
EVT FACE READY
```

Level A does not require real GC9A01 graphics. It only needs serial command parsing and explicit responses:

```text
OK FACE <COMMAND>
ERR FACE UNKNOWN_COMMAND
ERR FACE INVALID_ARGS
EVT FACE STATUS expression=<expr> look=<look> awake=<0|1>
```

Quick command checks after flashing:

```bash
python tools/send_command.py --port /dev/ttyUSB0 --line "SYS HEARTBEAT"
python tools/send_command.py --port /dev/ttyUSB0 --line "FACE STATUS"
python tools/face_demo.py --port /dev/ttyUSB0 --sequence basic
```

## Head ESP32

```bash
cd firmware/head_esp32
pio run
pio run --target upload
pio device monitor
```

Expected ready line:

```text
EVT HEAD READY
```

## Motor ESP32

```bash
cd firmware/motor_esp32
pio run
pio run --target upload
pio device monitor
```

Expected ready line:

```text
EVT MOTOR READY
```

Do not connect motor power during early firmware flashing.

## Lights ESP32

```bash
cd firmware/lights_esp32
pio run
pio run --target upload
pio device monitor
```

Expected ready line:

```text
EVT LIGHT READY
```

## Port Selection

If PlatformIO does not choose the right port:

```bash
pio run --target upload --upload-port /dev/ttyUSB0
pio device monitor --port /dev/ttyUSB0
```
