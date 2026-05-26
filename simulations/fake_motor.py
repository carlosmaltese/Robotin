from __future__ import annotations

from robotin.adapters.motor_adapter import MotorAdapter


def create() -> MotorAdapter:
    return MotorAdapter(name="motor", simulation=True)

