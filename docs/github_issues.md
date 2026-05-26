# Robotin GitHub Issues Proposal

## [Milestone 1: Foundation] Verify repository bootstrap

Labels:
- foundation
- testing

Depends on:
- None

Description:
Confirm that the initial repository can be installed, tested and run in simulation mode on a clean development machine.

Checklist:
- [ ] Install Python package in editable mode.
- [ ] Run the simulation entrypoint.
- [ ] Run the pytest suite.
- [ ] Confirm README commands match reality.

Acceptance criteria:
- [ ] Simulation prints the expected Robotin demo flow.
- [ ] All tests pass.
- [ ] README contains no broken setup commands.

Test commands:
```bash
cd raspberry
python -m pip install -e ".[dev]"
python -m robotin.main --simulation
pytest
```

## [Milestone 1: Foundation] Add development environment notes

Labels:
- documentation
- foundation

Depends on:
- Verify repository bootstrap

Description:
Expand development documentation with tested setup notes for Raspberry Pi OS, Windows and Linux.

Checklist:
- [ ] Document Python version requirement.
- [ ] Document virtual environment setup.
- [ ] Document optional pyserial install.
- [ ] Document PlatformIO install expectation.

Acceptance criteria:
- [ ] `docs/development.md` has setup steps for Python and PlatformIO.
- [ ] Hardware mode dependencies are clearly marked optional.

Test commands:
```bash
cd raspberry
python -m robotin.main --simulation
```

## [Milestone 1: Foundation] Add basic configuration validation

Labels:
- python
- config
- foundation

Depends on:
- Verify repository bootstrap

Description:
Add a small validation layer for `robot.yaml` and `devices.yaml` so missing required sections fail early with clear messages.

Checklist:
- [ ] Define required robot config keys.
- [ ] Define required device config keys.
- [ ] Add tests for valid config.
- [ ] Add tests for missing config fields.

Acceptance criteria:
- [ ] Invalid config raises a readable exception.
- [ ] Valid default config loads successfully.

Test commands:
```bash
cd raspberry
pytest
python -m robotin.main --simulation
```

## [Milestone 2: Face ESP32] Document dual GC9A01 wiring

Labels:
- hardware
- face
- documentation

Depends on:
- Add development environment notes

Description:
Turn the current face wiring TODO into a first practical wiring draft for two GC9A01 eye displays.

Checklist:
- [ ] Select shared SPI pins.
- [ ] Select separate CS pins.
- [ ] Document reset and backlight pins.
- [ ] Add power notes.
- [ ] Add known unknowns.

Acceptance criteria:
- [ ] `docs/wiring/face_gc9a01.md` includes a pin table.
- [ ] The document states whether both displays share SPI.
- [ ] Power and ground requirements are explicit.

Test commands:
```bash
python tools/face_demo.py --fake
```

## [Milestone 2: Face ESP32] Build face firmware skeleton

Labels:
- firmware
- face
- platformio

Depends on:
- Document dual GC9A01 wiring

Description:
Confirm the face ESP32 firmware skeleton builds under PlatformIO before real display drivers are added.

Checklist:
- [ ] Run PlatformIO build.
- [ ] Fix compile warnings or errors.
- [ ] Keep driver files as stubs.
- [ ] Document tested board target.

Acceptance criteria:
- [ ] `firmware/face_esp32` builds successfully.
- [ ] Firmware still prints `EVT FACE READY`.

Test commands:
```bash
cd firmware/face_esp32
pio run
```

## [Milestone 2: Face ESP32] Add face command smoke test script

Labels:
- tools
- face
- serial

Depends on:
- Build face firmware skeleton

Description:
Add or refine a smoke test flow for common face commands over fake mode and serial mode.

Checklist:
- [ ] Send neutral expression.
- [ ] Send happy expression.
- [ ] Send left, right and center look commands.
- [ ] Send blink.
- [ ] Print responses when using serial.

Acceptance criteria:
- [ ] Fake mode prints every command.
- [ ] Serial mode can target a selected port.

Test commands:
```bash
python tools/face_demo.py --fake
python tools/face_demo.py --port COM3
```

## [Milestone 3: Raspberry Serial Control] Add serial transport tests

Labels:
- python
- serial
- testing

Depends on:
- Add basic configuration validation

Description:
Test `SerialTransport` behavior without requiring real hardware by using a fake serial object or monkeypatching pyserial.

Checklist:
- [ ] Test line endings on send.
- [ ] Test read decoding.
- [ ] Test close behavior.
- [ ] Test missing pyserial error message.

Acceptance criteria:
- [ ] Serial tests run without hardware.
- [ ] Missing pyserial produces a clear runtime error only in hardware mode.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 3: Raspberry Serial Control] Add subsystem port configuration

Labels:
- python
- config
- serial

Depends on:
- Add serial transport tests

Description:
Connect `devices.yaml` to adapter creation so each subsystem can use its configured serial port in hardware mode.

Checklist:
- [ ] Read face port and baudrate.
- [ ] Read head port and baudrate.
- [ ] Read motor port and baudrate.
- [ ] Read lights port and baudrate.
- [ ] Keep simulation mode independent of pyserial.

Acceptance criteria:
- [ ] Simulation still runs with null ports.
- [ ] Hardware mode reports clear errors for missing ports.

Test commands:
```bash
cd raspberry
python -m robotin.main --simulation
pytest
```

## [Milestone 3: Raspberry Serial Control] Define acknowledgement handling

Labels:
- protocol
- serial
- raspberry

Depends on:
- Add subsystem port configuration

Description:
Define how adapters handle `OK`, `ERR` and timeout responses from ESP32 subsystems.

Checklist:
- [ ] Document response format.
- [ ] Add adapter send-and-read helper.
- [ ] Add timeout handling.
- [ ] Add tests for `OK` and `ERR`.

Acceptance criteria:
- [ ] Protocol docs describe acknowledgement behavior.
- [ ] Adapter tests cover success and error paths.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 4: AI Intent Routing] Add intent schema validation

Labels:
- ai
- schema
- testing

Depends on:
- Add basic configuration validation

Description:
Validate AI intent dictionaries before routing them to adapters.

Checklist:
- [ ] Check required fields.
- [ ] Restrict known priority values.
- [ ] Add tests for valid intent.
- [ ] Add tests for invalid intent.

Acceptance criteria:
- [ ] Invalid intent does not reach adapters.
- [ ] Error messages identify the invalid field.

Test commands:
```bash
cd raspberry
pytest tests/test_intent_router.py
```

## [Milestone 4: AI Intent Routing] Add more mock intents

Labels:
- ai
- simulation

Depends on:
- Add intent schema validation

Description:
Add a small set of mock intents for idle, greeting, thinking and error states.

Checklist:
- [ ] Add idle intent.
- [ ] Add greeting intent.
- [ ] Add thinking intent.
- [ ] Add error or confused intent.
- [ ] Add tests for routing each intent.

Acceptance criteria:
- [ ] Mock intents stay high-level.
- [ ] No mock intent contains direct motor commands.

Test commands:
```bash
cd raspberry
pytest
python -m robotin.main --simulation
```

## [Milestone 4: AI Intent Routing] Add intent router safety guard

Labels:
- ai
- safety
- python

Depends on:
- Add more mock intents

Description:
Ensure intent routing cannot directly trigger movement. Movement must remain behind explicit Raspberry-side command logic and safety checks.

Checklist:
- [ ] Document allowed intent fields.
- [ ] Reject direct motor fields in intent payloads.
- [ ] Add test for malicious or accidental motor intent.

Acceptance criteria:
- [ ] Direct motor intent is ignored or rejected.
- [ ] Motor adapter is not called by the intent router.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 5: Mouth Display] Choose mouth display module

Labels:
- hardware
- mouth
- documentation

Depends on:
- Document dual GC9A01 wiring

Description:
Choose the rectangular TFT mouth display candidate and document its interface, voltage and expected controller.

Checklist:
- [ ] Compare candidate displays.
- [ ] Pick one initial module.
- [ ] Document resolution and driver IC.
- [ ] Document wiring assumptions.

Acceptance criteria:
- [ ] A mouth display candidate is documented.
- [ ] Risks around SPI sharing are captured.

Test commands:
```bash
python tools/face_demo.py --fake
```

## [Milestone 5: Mouth Display] Define mouth command vocabulary

Labels:
- protocol
- mouth
- face

Depends on:
- Choose mouth display module

Description:
Define initial text commands for mouth states without implementing real graphics.

Checklist:
- [ ] Add neutral mouth command.
- [ ] Add talking mouth command.
- [ ] Add smile mouth command.
- [ ] Update protocol documentation.
- [ ] Add parser tests.

Acceptance criteria:
- [ ] Mouth commands are documented.
- [ ] Parser accepts the selected mouth commands.

Test commands:
```bash
cd raspberry
pytest tests/test_protocol_parser.py
```

## [Milestone 5: Mouth Display] Add fake mouth routing

Labels:
- python
- mouth
- simulation

Depends on:
- Define mouth command vocabulary

Description:
Route the `mouth` field from AI intents to the face adapter in fake mode.

Checklist:
- [ ] Add face adapter mouth method.
- [ ] Route `intent.mouth`.
- [ ] Add router test.
- [ ] Keep real display implementation out of scope.

Acceptance criteria:
- [ ] Simulation prints a mouth command when intent includes mouth state.
- [ ] Tests prove mouth routing works.

Test commands:
```bash
cd raspberry
python -m robotin.main --simulation
pytest
```

## [Milestone 6: Head Servos] Document head servo wiring and limits

Labels:
- hardware
- head
- safety

Depends on:
- Add development environment notes

Description:
Replace head servo wiring TODOs with selected pins, power notes and provisional mechanical limits.

Checklist:
- [ ] Select pan servo signal pin.
- [ ] Select tilt servo signal pin.
- [ ] Document external 5 V supply.
- [ ] Document common ground.
- [ ] Define provisional pan and tilt limits.

Acceptance criteria:
- [ ] Wiring doc includes pin table.
- [ ] Mechanical limit notes are visible before implementation.

Test commands:
```bash
python tools/head_demo.py --fake
```

## [Milestone 6: Head Servos] Build head firmware skeleton

Labels:
- firmware
- head
- platformio

Depends on:
- Document head servo wiring and limits

Description:
Confirm the head ESP32 firmware skeleton builds before attaching real servos.

Checklist:
- [ ] Run PlatformIO build.
- [ ] Fix compile warnings or errors.
- [ ] Keep servo driver as stub.
- [ ] Document tested board target.

Acceptance criteria:
- [ ] `firmware/head_esp32` builds successfully.
- [ ] Firmware prints `EVT HEAD READY`.

Test commands:
```bash
cd firmware/head_esp32
pio run
```

## [Milestone 6: Head Servos] Add head command limit validation

Labels:
- python
- head
- safety

Depends on:
- Build head firmware skeleton

Description:
Add Raspberry-side validation for pan and tilt command limits before sending head commands.

Checklist:
- [ ] Add configured pan range.
- [ ] Add configured tilt range.
- [ ] Reject out-of-range commands.
- [ ] Add tests for valid and invalid angles.

Acceptance criteria:
- [ ] Invalid angles never reach the adapter transport.
- [ ] Center command remains valid.

Test commands:
```bash
cd raspberry
pytest
python ../tools/head_demo.py --fake
```

## [Milestone 7: Vision] Define vision event model

Labels:
- vision
- architecture
- schema

Depends on:
- Add basic configuration validation

Description:
Define the first high-level vision events without integrating a real camera.

Checklist:
- [ ] Define event names.
- [ ] Define payload fields.
- [ ] Update event schema.
- [ ] Document that vision does not command motors directly.

Acceptance criteria:
- [ ] Vision event schema is documented.
- [ ] Events are high-level observations only.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 7: Vision] Add mock camera event publisher

Labels:
- vision
- simulation
- python

Depends on:
- Define vision event model

Description:
Extend the mock camera service so it can publish deterministic fake observations for tests and demos.

Checklist:
- [ ] Add fake observation output.
- [ ] Publish through event bus.
- [ ] Add test subscriber.
- [ ] Keep real camera out of scope.

Acceptance criteria:
- [ ] Mock camera can emit one known observation.
- [ ] Test verifies event payload.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 7: Vision] Add vision enable flag

Labels:
- vision
- config
- python

Depends on:
- Add mock camera event publisher

Description:
Add a config flag that allows vision to remain disabled by default and enabled only for explicit experiments.

Checklist:
- [ ] Add config option.
- [ ] Keep default disabled.
- [ ] Log whether vision is enabled.
- [ ] Add tests for default config.

Acceptance criteria:
- [ ] Simulation works with vision disabled.
- [ ] Enabling mock vision does not require camera hardware.

Test commands:
```bash
cd raspberry
python -m robotin.main --simulation
pytest
```

## [Milestone 8: Mobile Base] Document motor driver choice

Labels:
- hardware
- motors
- documentation

Depends on:
- Add development environment notes

Description:
Choose or shortlist the motor driver and document voltage, current and wiring assumptions.

Checklist:
- [ ] List candidate drivers.
- [ ] Pick initial driver or shortlist.
- [ ] Document motor voltage.
- [ ] Document current budget.
- [ ] Document emergency stop strategy.

Acceptance criteria:
- [ ] `docs/wiring/motors.md` includes driver notes.
- [ ] Power risks are explicitly documented.

Test commands:
```bash
python tools/motor_demo.py --fake
```

## [Milestone 8: Mobile Base] Build motor firmware skeleton

Labels:
- firmware
- motors
- platformio

Depends on:
- Document motor driver choice

Description:
Confirm the motor ESP32 firmware skeleton builds before real motor output is implemented.

Checklist:
- [ ] Run PlatformIO build.
- [ ] Fix compile warnings or errors.
- [ ] Keep motor output disabled.
- [ ] Document tested board target.

Acceptance criteria:
- [ ] `firmware/motor_esp32` builds successfully.
- [ ] Firmware prints `EVT MOTOR READY`.

Test commands:
```bash
cd firmware/motor_esp32
pio run
```

## [Milestone 8: Mobile Base] Add motor command duration requirement

Labels:
- motors
- safety
- protocol

Depends on:
- Build motor firmware skeleton

Description:
Require motion commands to include a bounded duration before any real motor control is enabled.

Checklist:
- [ ] Update motor command builder.
- [ ] Update parser tests.
- [ ] Update motor demo.
- [ ] Document duration requirement.

Acceptance criteria:
- [ ] Drive commands without duration are rejected for hardware mode.
- [ ] Fake mode can still show legacy examples only if marked safe.

Test commands:
```bash
cd raspberry
pytest tests/test_safety_manager.py
python ../tools/motor_demo.py --fake
```

## [Milestone 9: Obstacle Avoidance] Select obstacle sensor candidates

Labels:
- hardware
- obstacles
- documentation

Depends on:
- Document motor driver choice

Description:
Select candidate obstacle sensors and document their expected limitations.

Checklist:
- [ ] Compare ultrasonic, ToF and IR options.
- [ ] Pick initial front sensor candidate.
- [ ] Document blind spots.
- [ ] Document mounting assumptions.

Acceptance criteria:
- [ ] `tasks/phase_08_obstacles.md` or wiring docs include sensor notes.
- [ ] Safety limitations are explicit.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 9: Obstacle Avoidance] Define obstacle event schema

Labels:
- obstacles
- schema
- safety

Depends on:
- Select obstacle sensor candidates

Description:
Define obstacle events that can be consumed by safety logic without coupling sensors directly to motor commands.

Checklist:
- [ ] Define obstacle detected event.
- [ ] Define obstacle cleared event.
- [ ] Add distance field if needed.
- [ ] Add schema tests or validation notes.

Acceptance criteria:
- [ ] Obstacle events are high-level safety inputs.
- [ ] Motor commands are not emitted by sensor code.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 9: Obstacle Avoidance] Block forward motion on fake obstacle

Labels:
- obstacles
- safety
- testing

Depends on:
- Define obstacle event schema

Description:
Extend safety logic so a simulated obstacle can block forward motor commands.

Checklist:
- [ ] Add obstacle state to safety manager.
- [ ] Block forward drive when obstacle is active.
- [ ] Allow stop command.
- [ ] Add tests for blocked and clear states.

Acceptance criteria:
- [ ] Forward drive is blocked while obstacle is active.
- [ ] `MOTOR STOP` still works.

Test commands:
```bash
cd raspberry
pytest tests/test_safety_manager.py
```

## [Milestone 10: Power and Safety] Document power domains

Labels:
- power
- safety
- documentation

Depends on:
- Document motor driver choice
- Document head servo wiring and limits
- Document dual GC9A01 wiring

Description:
Create a practical first draft of Robotin power domains for Raspberry, ESP32 boards, displays, servos, LEDs and motors.

Checklist:
- [ ] Document Raspberry supply.
- [ ] Document ESP32 supply.
- [ ] Document servo supply.
- [ ] Document motor supply.
- [ ] Document common ground strategy.
- [ ] Document fuse or protection TODOs.

Acceptance criteria:
- [ ] `docs/wiring/power.md` includes a power-domain table.
- [ ] Unsafe power assumptions are called out clearly.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 10: Power and Safety] Add heartbeat watchdog policy

Labels:
- safety
- protocol
- firmware

Depends on:
- Define acknowledgement handling

Description:
Define and test the expected heartbeat behavior between Raspberry and ESP32 subsystems.

Checklist:
- [ ] Document heartbeat interval.
- [ ] Document timeout behavior.
- [ ] Add Raspberry watchdog tests.
- [ ] Add firmware TODOs for local motor stop.

Acceptance criteria:
- [ ] Safety docs state what happens on heartbeat loss.
- [ ] Watchdog tests pass.

Test commands:
```bash
cd raspberry
pytest
```

## [Milestone 10: Power and Safety] Add emergency stop integration test

Labels:
- safety
- motors
- testing

Depends on:
- Add motor command duration requirement
- Add heartbeat watchdog policy

Description:
Add an integration-style test proving emergency stop blocks motion through the adapter layer.

Checklist:
- [ ] Trigger emergency stop.
- [ ] Attempt motor drive.
- [ ] Confirm no drive command is sent.
- [ ] Clear emergency stop.
- [ ] Confirm movement can be allowed again after validation.

Acceptance criteria:
- [ ] Test proves safety manager blocks adapter output.
- [ ] Emergency reason is preserved for logging.

Test commands:
```bash
cd raspberry
pytest tests/test_safety_manager.py
```

