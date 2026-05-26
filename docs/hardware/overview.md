# Robotin Hardware Overview

Robotin uses a distributed physical architecture. The Raspberry Pi is the central computer and each ESP32 board owns one focused hardware domain.

## Main Blocks

| Block | Role | Notes |
| --- | --- | --- |
| Raspberry Pi | Main brain | Runs the `robotin` Python package, orchestration, voice, vision and safety policy. |
| Face ESP32 | Face controller | Drives the two GC9A01 eye displays now and may coordinate a future mouth display. |
| Head ESP32 | Head controller | Future pan/tilt servos and optional sound direction subsystem. |
| Motor ESP32 | Mobile base controller | Future DC motor driver control, local stop behavior and heartbeat monitoring. |
| Lights ESP32 or ESP32-C3 | Light controller | Simple LEDs first, WS2812B later. |
| USB microphone | Voice input | Connected to Raspberry Pi for AI and speech workflows. |
| Future webcam | Vision input | Connected to Raspberry Pi, disabled by default until the vision phase. |

## Communication

Initial internal control uses USB serial from Raspberry Pi to each ESP32 subsystem.

WiFi and Bluetooth are not used for internal robot control. They may be useful later for external development access, but not for safety-critical subsystem commands.

## Face Bring-up Strategy

The face subsystem starts with a serial-only foundation before any display driver work:

- Level A: validate USB serial, `EVT FACE READY`, `SYS HEARTBEAT`, `FACE STATUS`, expression, look, blink, sleep and wake commands.
- Level B: initialize one GC9A01, then two displays, then expression graphics.

This keeps protocol debugging separate from GC9A01 driver debugging.

## Naming Convention

- Robotin: visible robot and project name.
- `robotin`: repository, technical folders, Python package and commands.
