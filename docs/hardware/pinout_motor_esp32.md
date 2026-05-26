# Motor ESP32 Pinout

TODO: select motor driver before final pinout.

| Signal | Board Pin/GPIO | Voltage | Direction | Wire Color | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| USB_SERIAL | USB | 5 V USB | Bidirectional | USB cable | Yes | Control and flashing. |
| MOTOR_LEFT_PWM | TODO GPIO | 3.3 V | Output | Yellow | Future | Driver input. |
| MOTOR_LEFT_DIR | TODO GPIO | 3.3 V | Output | Green | Future | Driver input. |
| MOTOR_RIGHT_PWM | TODO GPIO | 3.3 V | Output | Yellow | Future | Driver input. |
| MOTOR_RIGHT_DIR | TODO GPIO | 3.3 V | Output | Green | Future | Driver input. |
| MOTOR_ENABLE | TODO GPIO | 3.3 V | Output | Red/white | Future | Must default disabled. |
| ESTOP_INPUT | TODO GPIO | 3.3 V | Input | Red/white | Future | Optional hard safety input. |
| ENCODER_LEFT_A | TODO GPIO | 3.3 V | Input | Blue | Future | If encoders are used. |
| ENCODER_RIGHT_A | TODO GPIO | 3.3 V | Input | Blue | Future | If encoders are used. |
| DRIVER_FAULT | TODO GPIO | 3.3 V | Input | Orange | Future | If motor driver supports fault output. |
| GND | GND | 0 V | Reference | Black | Yes | Common with motor driver logic GND. |

