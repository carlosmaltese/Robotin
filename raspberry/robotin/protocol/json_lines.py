from __future__ import annotations

import json
from typing import Any


def encode_message(message: dict[str, Any]) -> str:
    return json.dumps(message, separators=(",", ":"), ensure_ascii=True)


def decode_message(line: str) -> dict[str, Any]:
    data = json.loads(line)
    if not isinstance(data, dict):
        raise ValueError("JSON Lines message must be an object")
    return data

