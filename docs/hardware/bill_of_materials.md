# Bill of Materials

This is an initial planning BOM. Quantities and exact modules should be confirmed during hardware bring-up.

## Already Available

| Component | Quantity | Status | Purpose | Notes |
| --- | ---: | --- | --- | --- |
| Raspberry Pi 4B 8 GB | 1 | Available | Main brain for development | Future target may be Raspberry Pi 5 + AI HAT. |
| ESP32-WROOM board | Several | Available | Face, head, motor or lights controllers | Exact board pinout TODO. |
| ESP32-C3 board | Several | Available | Candidate for lights or small subsystem | Check USB serial and GPIO availability. |
| GC9A01 round displays | 2 | Available | Eye displays | Wiring and driver validation pending. |
| USB microphone | 1 | Available | Voice input | Connected to Raspberry Pi. |

## Recommended to Buy

| Component | Quantity | Status | Purpose | Notes |
| --- | ---: | --- | --- | --- |
| Powered USB hub | 1 | Recommended | Stable USB serial and peripherals | Prefer externally powered hub. |
| Buck converter 5 V, high current | 1-2 | Recommended | Logic and servo power rails | Size after current budget. |
| Fuse or polyfuse modules | Several | Recommended | Power protection | Add per power branch where practical. |
| Emergency stop button | 1 | Recommended | Physical motor power cut or safety input | Must be reachable during tests. |
| Dupont/JST connector kit | 1 | Recommended | Modular wiring | Use locking connectors for moving parts. |
| Large electrolytic capacitors | Several | Recommended | Reduce servo, motor and LED voltage dips | Start with TODO values after measurement. |

## Future

| Component | Quantity | Status | Purpose | Notes |
| --- | ---: | --- | --- | --- |
| Raspberry Pi 5 | 1 | Future | Higher performance brain | Planned upgrade path. |
| AI HAT | 1 | Future | Local AI acceleration | Interface and power impact TODO. |
| ESP32-S3 N16R8 with PSRAM | 1 | Future | More capable face controller | Good candidate for richer face graphics. |
| Rectangular TFT display | 1 | Future | Mouth display | Controller and resolution TODO. |
| Pan/tilt servos | 2 | Future | Head movement | Torque and stall current TODO. |
| DC motors | 2 | Future | Mobile base | Gear ratio and encoders TODO. |
| Motor driver | 1 | Future | Drive DC motors | Selection TODO. |
| Obstacle sensors | Several | Future | Safety and navigation | ToF/ultrasonic/IR tradeoff TODO. |
| WS2812B LEDs | TBD | Future | Rich light effects | Current budget must be calculated first. |

## Avoid

| Component | Quantity | Status | Purpose | Notes |
| --- | ---: | --- | --- | --- |
| Servo power from Raspberry 5 V pin | 0 | Avoid | Unsafe power shortcut | Causes resets and voltage dips. |
| Motor power from USB | 0 | Avoid | Unsafe power shortcut | Motors need a separate protected supply. |
| Loose breadboard for moving robot wiring | 0 | Avoid | Temporary prototyping only | Vibration causes intermittent faults. |
| WiFi/Bluetooth for internal control | 0 | Avoid | Internal subsystem control | Use USB serial for deterministic debugging. |

