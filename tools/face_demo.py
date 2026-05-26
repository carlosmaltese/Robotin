from __future__ import annotations

import argparse

from _path import add_raspberry_path

add_raspberry_path()

from robotin.adapters.face_adapter import FaceAdapter  # noqa: E402
from robotin.adapters.serial_transport import SerialTransport  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a face command demo")
    parser.add_argument(
        "--simulation",
        "--fake",
        action="store_true",
        help="Print commands without opening a serial port",
    )
    parser.add_argument("--port", help="Serial port for future hardware tests")
    parser.add_argument("--happy", action="store_true", help="Send a happy face command")
    parser.add_argument(
        "--sequence",
        choices=["basic"],
        default="basic",
        help="Demo sequence to run",
    )
    args = parser.parse_args()

    transport = None
    simulation = args.simulation or not args.port
    if not simulation and args.port:
        transport = SerialTransport(args.port)
        transport.connect()
    adapter = FaceAdapter(name="face", simulation=simulation, transport=transport)

    try:
        adapter.heartbeat()
        adapter.status()
        if args.happy:
            adapter.set_expression("happy")
            adapter.look("center")
            adapter.blink()
        elif args.sequence == "basic":
            adapter.wake()
            adapter.set_expression("neutral")
            adapter.look("center")
            adapter.set_expression("happy")
            adapter.look("left")
            adapter.look("right")
            adapter.look("center")
            adapter.blink()
            adapter.status()
    finally:
        if transport:
            transport.close()


if __name__ == "__main__":
    main()
