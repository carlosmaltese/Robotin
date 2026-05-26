# systemd Services

Robotin can later run as a Raspberry Pi system service. This is a future deployment target; during development, run it manually.

## Future Service Template

Create `/etc/systemd/system/robotin.service`:

```ini
[Unit]
Description=Robotin control service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/robotin/raspberry
Environment=PYTHONUNBUFFERED=1
ExecStart=/home/pi/robotin/raspberry/.venv/bin/python -m robotin.main --simulation
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

TODO: remove `--simulation` only after hardware configuration, watchdog behavior and emergency stop are validated.

## Commands

```bash
sudo systemctl daemon-reload
sudo systemctl enable robotin.service
sudo systemctl start robotin.service
sudo systemctl status robotin.service
```

View logs:

```bash
journalctl -u robotin.service -f
```

## Safety Notes

- Do not auto-start hardware motor control until E-STOP and heartbeat behavior are verified.
- Keep motors disabled by default.
- Use simulation service first.

