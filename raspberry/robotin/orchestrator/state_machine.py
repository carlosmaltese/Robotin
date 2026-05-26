from __future__ import annotations

from enum import Enum


class RobotState(str, Enum):
    BOOTING = "booting"
    IDLE = "idle"
    LISTENING = "listening"
    THINKING = "thinking"
    SPEAKING = "speaking"
    MOVING = "moving"
    ERROR = "error"
    EMERGENCY_STOP = "emergency_stop"
    SHUTDOWN = "shutdown"


class RobotStateMachine:
    def __init__(self) -> None:
        self.state = RobotState.BOOTING

    def mark_ready(self) -> None:
        if self.state == RobotState.BOOTING:
            self.state = RobotState.IDLE

    def activate(self) -> None:
        if self.state == RobotState.IDLE:
            self.state = RobotState.THINKING

    def listen(self) -> None:
        self.state = RobotState.LISTENING

    def think(self) -> None:
        self.state = RobotState.THINKING

    def speak(self) -> None:
        self.state = RobotState.SPEAKING

    def move(self) -> None:
        self.state = RobotState.MOVING

    def error(self) -> None:
        self.state = RobotState.ERROR

    def emergency_stop(self) -> None:
        self.state = RobotState.EMERGENCY_STOP

    def clear_emergency(self) -> None:
        if self.state == RobotState.EMERGENCY_STOP:
            self.state = RobotState.IDLE

    def shutdown(self) -> None:
        self.state = RobotState.SHUTDOWN
