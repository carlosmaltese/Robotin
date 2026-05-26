# Face ESP32 Pinout

TODO: confirm exact ESP32 board variant and display wiring before soldering.

The first FACE implementation is split into:

- Level A: serial firmware foundation with `FACE EXPR`, `FACE LOOK`, `FACE BLINK`, `FACE STATUS`, `FACE SLEEP`, `FACE WAKE` and `SYS HEARTBEAT`; no real display graphics.
- Level B: one GC9A01 display, then two GC9A01 displays, then expression rendering.

| Signal | Board Pin/GPIO | Voltage | Direction | Wire Color | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| USB_SERIAL | USB | 5 V USB | Bidirectional | USB cable | Yes | Control and flashing. |
| EYE_SPI_SCK | TODO GPIO | 3.3 V | Output | Purple | Yes | Shared by both GC9A01 displays. |
| EYE_SPI_MOSI | TODO GPIO | 3.3 V | Output | Gray | Yes | Display data. |
| EYE_LEFT_CS | TODO GPIO | 3.3 V | Output | Pink | Yes | Left eye chip select. |
| EYE_RIGHT_CS | TODO GPIO | 3.3 V | Output | Pink | Yes | Right eye chip select. |
| EYE_DC | TODO GPIO | 3.3 V | Output | Blue | Yes | Data/command line. Shared or separate TODO. |
| EYE_RST | TODO GPIO | 3.3 V | Output | White | Recommended | Reset line. Shared or separate TODO. |
| EYE_BL | TODO GPIO | 3.3 V | Output | Yellow | Recommended | Backlight control TODO. |
| DISPLAY_3V3 | 3V3 | 3.3 V | Power | Orange | Yes | Confirm current budget. |
| GND | GND | 0 V | Reference | Black | Yes | Common ground. |
| MOUTH_SPI_CS | TODO GPIO | 3.3 V | Output | Pink | Future | Future rectangular TFT. |

## Level A Serial Contract

USB serial is the only required connection for the first real FACE firmware task.

Expected startup event:

```text
EVT FACE READY
```

Expected status event:

```text
EVT FACE STATUS expression=<expr> look=<look> awake=<0|1>
```

Display pins remain TODO until Level B.
