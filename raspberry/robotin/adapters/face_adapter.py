from __future__ import annotations

from robotin.adapters.base import BaseAdapter
from robotin.protocol.messages import (
    face_blink,
    face_expr,
    face_look,
    face_mouth,
    face_sleep,
    face_status,
    face_wake,
    heartbeat,
)


class FaceAdapter(BaseAdapter):
    def set_expression(self, name: str) -> None:
        self.send(face_expr(name))

    def look(self, direction: str) -> None:
        self.send(face_look(direction))

    def set_mouth(self, state: str) -> None:
        self.send(face_mouth(state))

    def blink(self) -> None:
        self.send(face_blink())

    def sleep(self) -> None:
        self.send(face_sleep())

    def wake(self) -> None:
        self.send(face_wake())

    def status(self) -> None:
        self.send(face_status())

    def heartbeat(self) -> None:
        self.send(heartbeat())
