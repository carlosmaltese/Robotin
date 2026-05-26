# Robotin Raspberry

This directory contains the Raspberry Pi control layer for Robotin.

Run the simulation:

```bash
python -m robotin.main --simulation
```

Or from the repository root:

```bash
python tools/run_simulation.py
```

The simulation does not require hardware or pyserial.

Install dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Run one test file:

```bash
pytest tests/test_protocol_parser.py
```

From the repository root:

```bash
make test
```

If a test fails, read the first failure block. Parser failures usually mean command validation changed; simulation boot failures usually mean the fake startup flow changed.
