# Logs

Early Robotin logs go to the console. Future service deployment will use systemd journal output.

## Console Logs

Simulation output should stay direct and readable:

```text
[Robotin] starting in simulation mode
[face] FACE EXPR happy
[voice] Hola, soy Robotin.
```

## Subsystem Logs

ESP32 firmware should emit simple event lines:

```text
EVT FACE READY
EVT MOTOR FAULT overcurrent
```

## Levels

Use these levels in Raspberry logs when structured logging is added:

- INFO: startup, mode, subsystem ready, normal commands.
- WARNING: retries, missed heartbeat, degraded subsystem.
- ERROR: failed connection, rejected command, safety block.

## What to Record

- startup mode,
- config file paths,
- serial port mapping,
- subsystem ready events,
- safety state changes,
- command rejection reasons.

## What to Avoid Recording

- raw microphone audio,
- private speech transcripts unless explicitly enabled for debugging,
- secrets,
- full high-volume camera frames,
- noisy repeated heartbeat logs at INFO level.

