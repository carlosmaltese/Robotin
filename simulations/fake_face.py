from __future__ import annotations

from robotin.adapters.face_adapter import FaceAdapter


def create() -> FaceAdapter:
    return FaceAdapter(name="face", simulation=True)

