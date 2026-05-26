from __future__ import annotations


def main() -> None:
    try:
        from serial.tools import list_ports  # type: ignore
    except ImportError:
        print("pyserial is not installed. Install with: pip install pyserial")
        return

    ports = list(list_ports.comports())
    if not ports:
        print("No serial ports found")
        return
    for port in ports:
        print(f"{port.device}\t{port.description}")


if __name__ == "__main__":
    main()

