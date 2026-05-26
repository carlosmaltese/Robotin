# Wiring Conventions

Consistent wiring makes Robotin easier to debug and safer to modify.

## Wire Colors

| Signal Type | Recommended Color | Notes |
| --- | --- | --- |
| GND | Black | Use consistently. |
| 5 V | Red | Mark high-current branches separately. |
| 3.3 V | Orange | ESP32 logic rail. |
| UART TX | Yellow | Label direction at the source. |
| UART RX | Green | Label direction at the receiver. |
| I2C SDA | Blue | Pullups TODO per bus. |
| I2C SCL | White | Pullups TODO per bus. |
| SPI SCK | Purple | Shared SPI clock. |
| SPI MOSI | Gray | Display data out from controller. |
| SPI MISO | Brown | Often unused for displays. |
| SPI CS | Pink | One chip select per device. |
| E-STOP or safety | Red/white | Make it visually distinct. |

## UART Conventions

- TX from one board connects to RX on the other.
- RX from one board connects to TX on the other.
- USB serial is preferred for early phases.
- Use 115200 baud unless a subsystem document says otherwise.

## I2C Conventions

- Keep I2C wiring short.
- Document pullup voltage.
- Avoid mixing 5 V I2C devices with 3.3 V ESP32/Raspberry pins without level shifting.

## SPI Conventions

- Shared SCK and MOSI are acceptable for multiple displays.
- Each SPI device needs a dedicated CS line.
- Keep display wires short during early bring-up.
- TODO: confirm final GC9A01 SPI pinout.

## Cable Labels

Label both ends of every cable:

- subsystem name,
- signal name,
- voltage if power,
- connector name.

Example: `FACE_CONNECTOR / SPI_SCK`.

## Debugging Practices

- Test one subsystem at a time.
- Start with fake mode before hardware mode.
- Keep a wiring change log.
- Photograph working wiring before disassembly.
- Use a multimeter before connecting expensive boards.

