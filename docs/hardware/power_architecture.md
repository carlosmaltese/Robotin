# Power Architecture

Robotin must keep logic, servos, motors and high-current lighting separated enough to avoid resets and unsafe motion.

## Power Branches

| Branch | Loads | Notes |
| --- | --- | --- |
| Raspberry logic | Raspberry Pi, USB microphone, future webcam | Use a known-good Raspberry supply. |
| ESP32 logic | Face, head, motor and lights controllers | Can be USB-powered during development. Final wiring TODO. |
| Displays | GC9A01 eyes, future mouth TFT | Current budget TODO. Avoid brownouts on shared rails. |
| Servos | Future pan/tilt servos | Separate 5 V rail. Never power from Raspberry. |
| Motors | Future DC motors and driver | Separate motor supply with protection and E-STOP strategy. |
| LEDs | Simple LEDs or WS2812B | Separate branch if current grows. |

## Grounding

All control electronics that exchange signals must share GND. Power branches can be separate, but signal reference must be common.

TODO: draw final star-ground or distribution layout after physical chassis design.

## Protection

- Add fuse or polyfuse protection to high-current branches.
- Add reverse polarity protection where practical.
- Add a physical E-STOP that can disable motor power or assert a hard safety input.
- Keep motor enable disabled until software heartbeat and safety state are valid.

## Capacitors

Add bulk capacitance near:

- servo rail,
- motor driver input,
- LED strip input,
- display power if noise appears.

TODO: choose capacitor values after measuring current spikes.

## Buck Converters

Use buck converters sized above expected continuous current. Leave thermal margin and verify voltage under load.

## Safety Warnings

- Do not power motors from Raspberry Pi or USB.
- Do not test mobile base movement with wheels touching the ground until software limits and E-STOP are verified.
- Disconnect motor power while flashing or debugging unrelated subsystems.

