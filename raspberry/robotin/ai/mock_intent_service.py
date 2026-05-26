from __future__ import annotations

from robotin.ai.intent_schema import AIIntent


class MockIntentService:
    def next_intent(self) -> AIIntent:
        return AIIntent.from_dict(
            {
                "utterance": "Hola, soy Robotin.",
                "emotion": "happy",
                "gaze": "center",
                "mouth": "talking",
                "head": {"gesture": "small_nod"},
                "lights": {"mode": "warm"},
                "priority": "normal",
            }
        )

