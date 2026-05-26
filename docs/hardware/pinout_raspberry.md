# Raspberry Pi Pinout

Most early Robotin control uses USB serial, so Raspberry GPIO usage should remain minimal until a real need appears.

| Signal | Board Pin/GPIO | Voltage | Direction | Wire Color | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| USB_FACE_SERIAL | USB port | 5 V USB | Bidirectional | USB cable | Yes | Initial control path for face ESP32. |
| USB_HEAD_SERIAL | USB port | 5 V USB | Bidirectional | USB cable | Future | Initial control path for head ESP32. |
| USB_MOTOR_SERIAL | USB port | 5 V USB | Bidirectional | USB cable | Future | Initial control path for motor ESP32. |
| USB_LIGHT_SERIAL | USB port | 5 V USB | Bidirectional | USB cable | Future | Initial control path for lights ESP32. |
| USB_MIC | USB port | 5 V USB | Input | USB cable | Yes | Voice input. |
| USB_CAMERA | USB port | 5 V USB | Input | USB cable | Future | Vision phase. |
| ESTOP_INPUT | TODO GPIO | 3.3 V | Input | Red/white | Future | Optional safety input to Raspberry. |
| GND_REFERENCE | Physical pin 6 or TODO | 0 V | Reference | Black | Future | Only if using GPIO safety signals. |

