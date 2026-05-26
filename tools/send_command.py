from __future__ import annotations

import argparse

from _path import add_raspberry_path

add_raspberry_path()

from robotin.adapters.serial_transport import SerialTransport  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Send one Robotin serial command")
    parser.add_argument("--port", help="Serial port, for example COM3 or /dev/ttyUSB0")
    parser.add_argument("--baudrate", type=int, default=115200)
    parser.add_argument("--line", required=True, help="Command line to send")
    args = parser.parse_args()

    if not args.port:
        print(f"[fake-serial] {args.line}")
        return

    transport = SerialTransport(args.port, args.baudrate)
    transport.connect()
    try:
        transport.send_line(args.line)
        response = transport.read_line()
        if response:
            print(response)
    finally:
        transport.close()


if __name__ == "__main__":
    main()

