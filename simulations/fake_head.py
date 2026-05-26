from __future__ import annotations

from robotin.adapters.head_adapter import HeadAdapter


def create() -> HeadAdapter:
    return HeadAdapter(name="head", simulation=True)

