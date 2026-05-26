# Architecture

Robotin uses a simple distributed architecture:

- Raspberry Pi: orchestration, AI integration, voice, vision, safety policy and command routing.
- ESP32 face controller: eyes now, mouth later.
- ESP32 head controller: pan/tilt servos and future sound direction.
- ESP32 motor controller: future base movement and local motor safety.
- ESP32 lights controller: simple LEDs first, WS2812B later.

Internal control is USB serial. WiFi and Bluetooth are intentionally excluded from the control path.

## Responsibility Boundaries

The AI layer emits intentions such as emotion, gaze, utterance and light mood. It never sends raw motor or servo commands.

The Raspberry maps intentions to subsystem commands using adapters. Each adapter owns the command vocabulary for one subsystem.

The safety layer can block movement independently of the orchestrator. Motor commands must pass through `SafetyManager` before reaching hardware.

## Development Modes

- Simulation: fake adapters print commands to the console.
- Hardware: adapters use `SerialTransport` and pyserial.

Simulation is the default development path for early phases.

