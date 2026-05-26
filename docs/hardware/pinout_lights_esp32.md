# Lights ESP32 Pinout

This subsystem can use ESP32-WROOM or ESP32-C3 depending on available GPIO and LED requirements.

| Signal | Board Pin/GPIO | Voltage | Direction | Wire Color | Required | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| USB_SERIAL | USB | 5 V USB | Bidirectional | USB cable | Yes | Control and flashing. |
| LED_SIMPLE_1 | TODO GPIO | 3.3 V | Output | Yellow | Future | For simple LED output through resistor or driver. |
| LED_SIMPLE_2 | TODO GPIO | 3.3 V | Output | Yellow | Future | Optional. |
| WS2812_DATA | TODO GPIO | 3.3 V | Output | Green | Future | Level shifting TODO for longer strips. |
| LED_5V | External rail | 5 V | Power | Red | Future | Current budget required for WS2812B. |
| LED_GND | External rail GND | 0 V | Reference | Black | Future | Common with ESP32 GND. |
| GND | GND | 0 V | Reference | Black | Yes | Common ground. |

