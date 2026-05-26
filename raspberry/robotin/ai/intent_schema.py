from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class HeadIntent:
    gesture: str | None = None


@dataclass(frozen=True)
class LightIntent:
    mode: str = "idle"


@dataclass(frozen=True)
class AIIntent:
    utterance: str
    emotion: str = "neutral"
    gaze: str = "center"
    mouth: str = "neutral"
    head: HeadIntent = field(default_factory=HeadIntent)
    lights: LightIntent = field(default_factory=LightIntent)
    priority: str = "normal"

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AIIntent":
        head_data = data.get("head") if isinstance(data.get("head"), dict) else {}
        light_data = data.get("lights") if isinstance(data.get("lights"), dict) else {}
        return cls(
            utterance=str(data.get("utterance", "")),
            emotion=str(data.get("emotion", "neutral")),
            gaze=str(data.get("gaze", "center")),
            mouth=str(data.get("mouth", "neutral")),
            head=HeadIntent(gesture=head_data.get("gesture")),  # type: ignore[union-attr]
            lights=LightIntent(mode=str(light_data.get("mode", "idle"))),  # type: ignore[union-attr]
            priority=str(data.get("priority", "normal")),
        )

