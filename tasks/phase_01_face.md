# Phase 01: Eyes with ESP32

## Objective

Bring up the face ESP32 in two levels: first a serial foundation, then GC9A01 display rendering.

## Scope

- Level A: serial firmware only.
- Level B: one GC9A01 display, then two displays, then expressions.
- Validate wiring notes before display work.
- Confirm serial commands for expressions, gaze, blink, sleep, wake and status.

## Checklist

- [ ] Prepare minimal serial firmware.
- [ ] Respond `EVT FACE READY` on boot.
- [ ] Implement FACE command parser.
- [ ] Implement `OK FACE <COMMAND>`.
- [ ] Implement `ERR FACE UNKNOWN_COMMAND`.
- [ ] Implement `ERR FACE INVALID_ARGS`.
- [ ] Implement `EVT FACE STATUS expression=<expr> look=<look> awake=<0|1>`.
- [ ] Test with serial monitor.
- [ ] Test from `tools/send_command.py`.
- [ ] Test from `tools/face_demo.py --sequence basic`.
- [ ] Document real pinout for one eye.
- [ ] Test one GC9A01.
- [ ] Test two GC9A01.
- [ ] Add basic expressions.
- [ ] Build `firmware/face_esp32`.
- [ ] Send `FACE EXPR happy`.
- [ ] Send `FACE LOOK center`.
- [ ] Send `FACE BLINK`.
- [ ] Send `FACE STATUS`.

## Acceptance Criteria

- Firmware prints `EVT FACE READY`.
- Known face commands return `OK FACE <COMMAND>`.
- Unknown commands return `ERR FACE UNKNOWN_COMMAND`.
- Invalid arguments return `ERR FACE INVALID_ARGS`.
- `FACE STATUS` reports expression, look and awake state.
- Level A works without GC9A01 displays connected.

## Risks

- Incorrect SPI wiring.
- Display current above regulator budget.
- Debugging serial protocol and display driver at the same time.

## Hardware Notes

Use USB serial for control. Do not power displays from a weak supply. Keep Level A serial-only until the command contract is stable.

## Test Commands

```bash
python tools/face_demo.py --simulation
python tools/send_command.py --port /dev/ttyUSB0 --line "SYS HEARTBEAT"
python tools/send_command.py --port /dev/ttyUSB0 --line "FACE STATUS"
python tools/send_command.py --port /dev/ttyUSB0 --line "FACE EXPR happy"
python tools/face_demo.py --port /dev/ttyUSB0 --sequence basic
```
