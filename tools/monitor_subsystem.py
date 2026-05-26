from __future__ import annotations

import argparse

from _path import add_raspberry_path

add_raspberry_path()

from robotin.adapters.serial_transport import SerialTransport  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Monitor a Robotin serial subsystem")
    parser.add_argument("--port", required=True)
    parser.add_argument("--baudrate", type=int, default=115200)
    args = parser.parse_args()

    transport = SerialTransport(args.port, args.baudrate)
    transport.connect()
    try:
        while True:
            line = transport.read_line()
            if line:
                print(line)
    except KeyboardInterrupt:
        pass
    finally:
        transport.close()


if __name__ == "__main__":
    main()

