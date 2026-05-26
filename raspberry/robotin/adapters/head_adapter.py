from __future__ import annotations

from robotin.adapters.base import BaseAdapter
from robotin.protocol.messages import head_gesture, head_look


class HeadAdapter(BaseAdapter):
    def look(self, pan_deg: float, tilt_deg: float) -> None:
        self.send(head_look(pan_deg, tilt_deg))

    def center(self) -> None:
        self.look(0, 0)

    def gesture(self, name: str) -> None:
        self.send(head_gesture(name))

