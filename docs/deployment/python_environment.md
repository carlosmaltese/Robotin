# Python Environment

Robotin uses `Robotin` as the visible project name and `robotin` as the Python package name.

## Virtual Environment

Create the environment inside `raspberry`:

```bash
cd raspberry
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

On Windows PowerShell:

```powershell
cd raspberry
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## Editable Install

```bash
python -m pip install -e ".[dev]"
```

For real serial ports:

```bash
python -m pip install -e ".[dev,serial]"
```

## Tests

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_protocol_parser.py
```

Run a specific test:

```bash
pytest tests/test_simulation_boot.py::test_simulation_boot_runs_without_hardware
```

From the repository root:

```bash
make test
```

## Interpreting Basic Failures

- `ModuleNotFoundError`: activate the virtual environment or install with `python -m pip install -e ".[dev]"`.
- Parser assertion failure: check `robotin/protocol/parser.py` and `robotin/protocol/messages.py`.
- Simulation boot failure: check `robotin.main`, config loading and fake adapter output.
- Safety failure: do not proceed with motor hardware work until the failing behavior is understood.

## Run Simulation

From `raspberry`:

```bash
python -m robotin.main --simulation
```

From the repository root:

```bash
python tools/run_simulation.py
```

Simulation mode uses fake adapters and does not require pyserial or connected hardware.

## Package Structure

The package lives in `raspberry/robotin`:

- `robotin.main`: executable entrypoint.
- `robotin.orchestrator`: state machine and intent routing.
- `robotin.adapters`: subsystem adapters.
- `robotin.protocol`: text protocol and future JSON Lines helpers.
- `robotin.safety`: emergency stop, validation and watchdog logic.
- `robotin.ai`, `robotin.voice`, `robotin.vision`: mock service boundaries.
