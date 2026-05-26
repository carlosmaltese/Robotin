# Logical Connectors

These are logical connector definitions for documentation and labeling. Physical connector families are TODO.

## FACE_CONNECTOR

Purpose: connect face ESP32 to eye displays and future mouth display.

Signals:

- 3.3 V display power
- GND
- SPI SCK
- SPI MOSI
- left eye CS
- right eye CS
- display DC
- display reset
- display backlight
- future mouth CS

## HEAD_CONNECTOR

Purpose: connect head ESP32 to pan/tilt servos and future sound direction hardware.

Signals:

- servo 5 V
- servo GND
- pan PWM
- tilt PWM
- optional microphone signals
- ESP32 GND reference

## MOTOR_CONNECTOR

Purpose: connect motor ESP32 to motor driver and safety inputs.

Signals:

- left PWM
- left direction
- right PWM
- right direction
- motor enable
- driver fault input
- optional encoder inputs
- logic GND

## LIGHT_CONNECTOR

Purpose: connect lights ESP32 or ESP32-C3 to simple LEDs or WS2812B.

Signals:

- LED 5 V if needed
- LED GND
- simple LED outputs
- WS2812 data

## ESTOP_CONNECTOR

Purpose: expose physical emergency stop wiring.

Signals:

- E-STOP switch input
- optional motor power cut loop
- GND reference if using logic input

TODO: decide whether E-STOP cuts motor power directly, signals controllers, or both.

## POWER_DISTRIBUTION

Purpose: distribute protected power branches.

Branches:

- Raspberry supply
- ESP32 logic
- display power
- servo power
- motor power
- LED power

TODO: define connector current ratings and fuse values.

