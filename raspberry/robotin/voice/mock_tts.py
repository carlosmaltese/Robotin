from __future__ import annotations


class MockTTS:
    def __init__(self) -> None:
        self.spoken: list[str] = []

    def speak(self, text: str) -> None:
        self.spoken.append(text)
        print(f"[voice] {text}")
