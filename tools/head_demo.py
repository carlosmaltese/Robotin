from __future__ import annotations

import argparse

from _path import add_raspberry_path

add_raspberry_path()

from robotin.adapters.head_adapter import HeadAdapter  # noqa: E402
from robotin.adapters.serial_transport import SerialTransport  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a head command demo")
    parser.add_argument("--fake", action="store_true")
    parser.add_argument("--port")
    args = parser.parse_args()

    transport = None
    if not args.fake and args.port:
        transport = SerialTransport(args.port)
        transport.connect()
    adapter = HeadAdapter(name="head", simulation=args.fake or not args.port, transport=transport)

    try:
        adapter.center()
        adapter.look(15, -5)
        adapter.gesture("small_nod")
        adapter.center()
    finally:
        if transport:
            transport.close()


if __name__ == "__main__":
    main()

