# Head ESP32 Pinout

TODO: define servo pins after mechanical layout and servo selection.

| Signal | Board Pin/GPIO | Voltage | Direction | Wire Color | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| USB_SERIAL | USB | 5 V USB | Bidirectional | USB cable | Yes | Control and flashing. |
| PAN_SERVO_PWM | TODO GPIO | 3.3 V signal | Output | Yellow | Future | Servo power must be external 5 V. |
| TILT_SERVO_PWM | TODO GPIO | 3.3 V signal | Output | Yellow | Future | Servo power must be external 5 V. |
| SERVO_5V | External rail | 5 V | Power | Red | Future | Do not source from ESP32 or Raspberry. |
| SERVO_GND | External rail GND | 0 V | Reference | Black | Future | Common with ESP32 GND. |
| SOUND_MIC_1 | TODO GPIO/ADC/I2S | TBD | Input | Blue | Future | Sound direction phase. |
| SOUND_MIC_2 | TODO GPIO/ADC/I2S | TBD | Input | Blue | Future | Sound direction phase. |
| GND | GND | 0 V | Reference | Black | Yes | Common ground. |

