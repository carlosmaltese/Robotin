from __future__ import annotations

import argparse

from _path import add_raspberry_path

add_raspberry_path()

from robotin.adapters.motor_adapter import MotorAdapter  # noqa: E402
from robotin.adapters.serial_transport import SerialTransport  # noqa: E402
from robotin.safety.safety_manager import SafetyManager  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a safe motor command demo")
    parser.add_argument("--fake", action="store_true")
    parser.add_argument("--port")
    args = parser.parse_args()

    safety = SafetyManager(max_motor_power=0.3, max_duration_ms=1000)
    transport = None
    if not args.fake and args.port:
        transport = SerialTransport(args.port)
        transport.connect()
    adapter = MotorAdapter(
        name="motor",
        simulation=args.fake or not args.port,
        transport=transport,
        safety=safety,
    )

    try:
        adapter.drive(0.2, 0.2, duration_ms=500)
        adapter.stop()
    finally:
        if transport:
            transport.close()


if __name__ == "__main__":
    main()

