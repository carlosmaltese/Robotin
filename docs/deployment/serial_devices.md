# Serial Devices

Robotin initially uses USB serial for internal subsystem control.

## List Linux Serial Ports

```bash
ls -l /dev/ttyUSB*
ls -l /dev/ttyACM*
```

If no devices match, the shell may print an error. That can simply mean no board is connected.

## Use Robotin Tool

```bash
python tools/list_serial_devices.py
```

## Permissions

On Raspberry Pi OS or Debian-like systems, serial access often requires membership in `dialout`:

```bash
sudo usermod -aG dialout $USER
```

Log out and back in after changing group membership.

## Changing Port Names

ESP32 boards may appear as different ports after reconnecting:

- `/dev/ttyUSB0`
- `/dev/ttyUSB1`
- `/dev/ttyACM0`

Future stable names can be created with udev rules:

- `/dev/robotin-face`
- `/dev/robotin-head`
- `/dev/robotin-motor`
- `/dev/robotin-lights`

TODO: add udev rules after USB vendor/product IDs and serial numbers are known.

## Quick Manual Test

```bash
python tools/send_command.py --port /dev/ttyUSB0 --line "SYS HEARTBEAT"
python tools/monitor_subsystem.py --port /dev/ttyUSB0
```

