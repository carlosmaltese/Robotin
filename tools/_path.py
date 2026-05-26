from __future__ import annotations

import sys
from pathlib import Path


def add_raspberry_path() -> None:
    root = Path(__file__).resolve().parents[1]
    raspberry = root / "raspberry"
    if str(raspberry) not in sys.path:
        sys.path.insert(0, str(raspberry))

