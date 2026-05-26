# Troubleshooting

## ESP32 Does Not Appear

- Try another USB cable.
- Use a data-capable cable, not charge-only.
- Check `ls /dev/ttyUSB*` and `ls /dev/ttyACM*`.
- Check `python tools/list_serial_devices.py`.
- Try another USB port or powered hub.

## Permission Denied on Serial Port

Add the user to `dialout`:

```bash
sudo usermod -aG dialout $USER
```

Log out and back in.

## Serial Port Changes

Use `tools/list_serial_devices.py` before running hardware commands. Stable udev names are planned:

- `/dev/robotin-face`
- `/dev/robotin-head`
- `/dev/robotin-motor`
- `/dev/robotin-lights`

## Firmware Does Not Flash

- Hold BOOT while upload starts if the board requires it.
- Disconnect motor or servo power.
- Close serial monitors using the same port.
- Check PlatformIO board target.

## Display Does Not Respond

- Verify display power voltage.
- Verify GND.
- Confirm SPI SCK and MOSI.
- Confirm CS, DC and reset pins.
- Reduce wire length.
- TODO: confirm final GC9A01 library and pin mapping.

## Noise on Display

- Shorten SPI wires.
- Lower SPI speed.
- Add local decoupling capacitor.
- Check power rail stability.
- Keep motor and servo wiring away from display signals.

## Servo Vibrates

- Use external 5 V servo power.
- Confirm common GND.
- Check PWM pin.
- Check servo limits.
- Avoid commanding mechanical end stops.

## Motor Does Not Turn

- Confirm motor power is connected.
- Confirm driver enable pin.
- Confirm E-STOP state.
- Confirm safety manager permits movement.
- Test with wheels lifted.

## Raspberry Pi Reboots

Likely voltage drop or overloaded supply.

- Use official or high-quality Raspberry supply.
- Do not power servos or motors from Raspberry.
- Use a powered USB hub for multiple ESP32 boards.
- Check buck converter current rating.

