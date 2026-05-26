from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class LineTransport(Protocol):
    def send_line(self, line: str) -> None:
        ...


@dataclass
class BaseAdapter:
    name: str
    transport: LineTransport | None = None
    simulation: bool = True
    sent_lines: list[str] = field(default_factory=list)

    def send(self, line: str) -> None:
        self.sent_lines.append(line)
        if self.simulation:
            print(f"[{self.name}] {line}")
            return
        if self.transport is None:
            raise RuntimeError(f"No transport configured for {self.name}")
        self.transport.send_line(line)

