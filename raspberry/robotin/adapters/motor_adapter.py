from __future__ import annotations

from robotin.adapters.base import BaseAdapter
from robotin.protocol.messages import motor_drive, motor_stop
from robotin.safety.safety_manager import SafetyManager


class MotorAdapter(BaseAdapter):
    def __init__(
        self,
        name: str = "motor",
        safety: SafetyManager | None = None,
        **kwargs: object,
    ) -> None:
        super().__init__(name=name, **kwargs)
        self.safety = safety or SafetyManager()

    def drive(self, left: float, right: float, duration_ms: int | None = None) -> None:
        self.safety.validate_motor_command(left, right, duration_ms)
        if not self.safety.can_move():
            print("[safety] motor drive blocked by emergency stop")
            return
        self.send(motor_drive(left, right, duration_ms))

    def stop(self) -> None:
        self.send(motor_stop())
