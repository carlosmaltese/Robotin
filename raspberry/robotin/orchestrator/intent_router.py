from __future__ import annotations

from dataclasses import dataclass

from robotin.adapters.face_adapter import FaceAdapter
from robotin.adapters.head_adapter import HeadAdapter
from robotin.adapters.light_adapter import LightAdapter
from robotin.ai.intent_schema import AIIntent
from robotin.voice.mock_tts import MockTTS


@dataclass
class IntentRouter:
    face: FaceAdapter
    head: HeadAdapter
    lights: LightAdapter
    voice: MockTTS

    def route(self, intent: AIIntent) -> None:
        self.face.set_expression(intent.emotion)
        self.face.look(intent.gaze)
        self.face.set_mouth(intent.mouth)
        self.lights.set_mode(intent.lights.mode)
        if intent.head.gesture:
            self.head.gesture(intent.head.gesture)
        if intent.utterance:
            self.voice.speak(intent.utterance)
