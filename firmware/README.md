# Robotin Firmware

Each subdirectory is a minimal PlatformIO project for one ESP32 subsystem.

Current firmware goals:

- initialize `Serial` at 115200,
- print `EVT <SUBSYSTEM> READY`,
- read line-based commands,
- respond `OK` for known commands,
- respond `ERR unknown command` for unknown commands.

No display, servo, motor or LED drivers are implemented yet.

## Face Level A Contract

The next face firmware task should upgrade `firmware/face_esp32` from the generic skeleton responses to:

```text
EVT FACE READY
OK FACE <COMMAND>
ERR FACE UNKNOWN_COMMAND
ERR FACE INVALID_ARGS
EVT FACE STATUS expression=<expr> look=<look> awake=<0|1>
```

This is still serial-only and must not require GC9A01 graphics.
