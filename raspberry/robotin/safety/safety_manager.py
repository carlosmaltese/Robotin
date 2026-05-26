from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SafetyManager:
    max_motor_power: float = 1.0
    max_duration_ms: int = 5000
    emergency_stop: bool = False
    emergency_reason: str | None = None

    def trigger_emergency_stop(self, reason: str) -> None:
        self.emergency_stop = True
        self.emergency_reason = reason

    def clear_emergency_stop(self) -> None:
        self.emergency_stop = False
        self.emergency_reason = None

    def can_move(self) -> bool:
        return not self.emergency_stop

    def validate_motor_command(
        self, left: float, right: float, duration_ms: int | None = None
    ) -> None:
        for value in (left, right):
            if value < -self.max_motor_power or value > self.max_motor_power:
                raise ValueError(
                    f"Motor power {value} outside +/-{self.max_motor_power}"
                )
        if duration_ms is not None and (
            duration_ms <= 0 or duration_ms > self.max_duration_ms
        ):
            raise ValueError(
                f"Motor duration {duration_ms} outside 1..{self.max_duration_ms} ms"
            )

