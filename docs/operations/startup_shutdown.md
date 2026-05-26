# Startup and Shutdown

## Startup

Use this order during hardware tests:

1. Verify E-STOP is accessible.
2. Connect logic power.
3. Boot Raspberry Pi.
4. Connect or power ESP32 microcontrollers.
5. Confirm each subsystem prints a ready event.
6. Start Robotin in simulation or hardware mode.
7. Confirm heartbeat behavior.
8. Enable servos only after limits are configured.
9. Enable motor power last.

Motors should remain disabled until safety checks pass.

## Shutdown

Use this order:

1. Stop motors.
2. Center head if it is safe to move.
3. Stop face and light animations.
4. Stop Robotin services.
5. Shut down Raspberry Pi.
6. Cut motor, servo and LED power.
7. Cut logic power.

## Emergency Shutdown

If unexpected movement occurs:

1. Hit E-STOP.
2. Remove motor power.
3. Stop the Robotin process.
4. Inspect logs and wiring before retrying.

