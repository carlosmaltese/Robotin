from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    return subprocess.call(
        [sys.executable, "-m", "robotin.main", "--simulation"],
        cwd=root / "raspberry",
    )


if __name__ == "__main__":
    raise SystemExit(main())

