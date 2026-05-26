.PHONY: install test run-sim lint list-serial send-face-happy

install:
	cd raspberry && python -m pip install -e ".[dev]"

test:
	cd raspberry && pytest

run-sim:
	cd raspberry && python -m robotin.main --simulation

lint:
	cd raspberry && python -m compileall robotin tests

list-serial:
	python tools/list_serial_devices.py

send-face-happy:
	python tools/send_command.py --line "FACE EXPR happy"
