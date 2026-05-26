from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from robotin.adapters.face_adapter import FaceAdapter
from robotin.adapters.head_adapter import HeadAdapter
from robotin.adapters.light_adapter import LightAdapter
from robotin.adapters.motor_adapter import MotorAdapter
from robotin.ai.intent_schema import AIIntent
from robotin.orchestrator.intent_router import IntentRouter
from robotin.orchestrator.state_machine import RobotStateMachine
from robotin.safety.safety_manager import SafetyManager
from robotin.voice.mock_tts import MockTTS


@dataclass
class Orchestrator:
    config: dict[str, Any]
    safety: SafetyManager
    simulation: bool = True

    def __post_init__(self) -> None:
        self.state_machine = RobotStateMachine()
        self.face = FaceAdapter(name="face", simulation=self.simulation)
        self.head = HeadAdapter(name="head", simulation=self.simulation)
        self.motor = MotorAdapter(
            name="motor", simulation=self.simulation, safety=self.safety
        )
        self.lights = LightAdapter(name="light", simulation=self.simulation)
        self.voice = MockTTS()
        self.intent_router = IntentRouter(
            face=self.face,
            head=self.head,
            lights=self.lights,
            voice=self.voice,
        )

    def start(self) -> None:
        self.state_machine.mark_ready()
        print("[robotin] orchestrator started")

    def handle_intent(self, intent: AIIntent) -> None:
        self.state_machine.activate()
        self.intent_router.route(intent)

    def stop(self) -> None:
        self.state_machine.shutdown()
