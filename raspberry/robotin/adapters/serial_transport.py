from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SerialTransport:
    port: str
    baudrate: int = 115200
    timeout: float = 1.0

    def __post_init__(self) -> None:
        self._serial = None

    def connect(self) -> None:
        try:
            import serial  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "pyserial is required for hardware mode. Install with `pip install pyserial`."
            ) from exc
        self._serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def send_line(self, line: str) -> None:
        if self._serial is None:
            raise RuntimeError("SerialTransport is not connected")
        self._serial.write((line.rstrip("\r\n") + "\n").encode("utf-8"))

    def read_line(self) -> str | None:
        if self._serial is None:
            raise RuntimeError("SerialTransport is not connected")
        data = self._serial.readline()
        if not data:
            return None
        return data.decode("utf-8", errors="replace").strip()

    def close(self) -> None:
        if self._serial is not None:
            self._serial.close()
            self._serial = None

