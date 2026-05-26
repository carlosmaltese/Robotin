# Raspberry Pi Setup

These steps prepare a Raspberry Pi for Robotin development.

## Base System

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git python3-venv python3-pip minicom picocom
```

Optional but useful:

```bash
sudo apt install -y build-essential curl
```

## Clone Repository

```bash
git clone <repo-url> robotin
cd robotin
```

## Create Python Environment

```bash
cd raspberry
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Install serial support when hardware is connected:

```bash
python -m pip install -e ".[dev,serial]"
```

## Run Simulation

```bash
python -m robotin.main --simulation
```

Expected result:

```text
[robotin] starting in simulation mode
[robotin] loading configuration
[robotin] orchestrator started
[face] FACE EXPR happy
[face] FACE LOOK center
[face] FACE MOUTH talking
[light] LIGHT MODE warm
[head] HEAD GESTURE small_nod
[voice] Hola, soy Robotin.
[robotin] demo completed
```

## Run Tests

```bash
pytest
```
