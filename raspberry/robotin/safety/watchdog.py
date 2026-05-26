from __future__ import annotations

import time
from dataclasses import dataclass, field


@dataclass
class Watchdog:
    timeout_s: float
    last_heartbeat: float = field(default_factory=time.monotonic)

    def heartbeat(self) -> None:
        self.last_heartbeat = time.monotonic()

    def expired(self) -> bool:
        return time.monotonic() - self.last_heartbeat > self.timeout_s

