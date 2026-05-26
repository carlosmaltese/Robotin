# Face GC9A01 Wiring

The face subsystem bring-up is intentionally staged.

## Level A: Serial Foundation

No GC9A01 graphics are required.

Required:

- ESP32 connected by USB serial.
- Firmware prints `EVT FACE READY`.
- Firmware accepts `SYS HEARTBEAT`.
- Firmware accepts `FACE STATUS`.
- Firmware accepts `FACE EXPR`, `FACE LOOK`, `FACE BLINK`, `FACE SLEEP` and `FACE WAKE`.
- Firmware returns `OK FACE <COMMAND>` or `ERR FACE <REASON>`.

## Level B: Display Bring-up

Bring up graphics in this order:

1. Initialize one GC9A01 display.
2. Draw a static test pattern.
3. Initialize two GC9A01 displays on shared SPI with separate CS lines.
4. Add basic eye positions.
5. Add expression rendering.

TODO:

- Confirm exact ESP32 board pinout.
- Document SPI pins for both GC9A01 displays.
- Decide if both displays share SPI with separate CS pins.
- Add power budget and level notes.
- Add reset/backlight control pins.

No final wiring is defined yet.
