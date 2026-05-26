from __future__ import annotations

from robotin.adapters.light_adapter import LightAdapter


def create() -> LightAdapter:
    return LightAdapter(name="light", simulation=True)

