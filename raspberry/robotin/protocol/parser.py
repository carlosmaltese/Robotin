from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    subsystem: str
    action: str
    args: tuple[str, ...]

    @property
    def target(self) -> str:
        return self.subsystem

    @property
    def command(self) -> str:
        return self.action


def _require_arg_count(
    subsystem: str,
    action: str,
    args: tuple[str, ...],
    allowed_counts: set[int],
) -> None:
    if len(args) not in allowed_counts:
        allowed = ", ".join(str(count) for count in sorted(allowed_counts))
        raise ValueError(
            f"{subsystem} {action} expected {allowed} args, got {len(args)}"
        )


def _require_float(value: str, name: str) -> None:
    try:
        float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be numeric, got {value!r}") from exc


def _require_int(value: str, name: str) -> None:
    try:
        int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {value!r}") from exc


def parse_line(line: str) -> Command:
    parts = line.strip().split()
    if len(parts) < 2:
        raise ValueError(f"Invalid command line: {line!r}")

    subsystem = parts[0].upper()
    action = parts[1].upper()
    args = tuple(parts[2:])

    known = {
        ("FACE", "EXPR"),
        ("FACE", "LOOK"),
        ("FACE", "MOUTH"),
        ("FACE", "BLINK"),
        ("FACE", "STATUS"),
        ("FACE", "SLEEP"),
        ("FACE", "WAKE"),
        ("HEAD", "LOOK"),
        ("HEAD", "GESTURE"),
        ("HEAD", "CENTER"),
        ("MOTOR", "DRIVE"),
        ("MOTOR", "STOP"),
        ("LIGHT", "MODE"),
        ("SYS", "HEARTBEAT"),
    }
    if (subsystem, action) not in known:
        raise ValueError(f"Unknown command: {subsystem} {action}")

    _validate_args(subsystem, action, args)
    return Command(subsystem=subsystem, action=action, args=args)


def _validate_args(subsystem: str, action: str, args: tuple[str, ...]) -> None:
    if subsystem == "FACE" and action in {"EXPR", "LOOK", "MOUTH"}:
        _require_arg_count(subsystem, action, args, {1})
    elif subsystem == "FACE" and action in {"BLINK", "STATUS", "SLEEP", "WAKE"}:
        _require_arg_count(subsystem, action, args, {0})
    elif subsystem == "HEAD" and action == "LOOK":
        _require_arg_count(subsystem, action, args, {2})
        _require_float(args[0], "pan_deg")
        _require_float(args[1], "tilt_deg")
    elif subsystem == "HEAD" and action == "GESTURE":
        _require_arg_count(subsystem, action, args, {1})
    elif subsystem == "HEAD" and action == "CENTER":
        _require_arg_count(subsystem, action, args, {0})
    elif subsystem == "MOTOR" and action == "DRIVE":
        _require_arg_count(subsystem, action, args, {2, 3})
        _require_float(args[0], "left")
        _require_float(args[1], "right")
        if len(args) == 3:
            _require_int(args[2], "duration_ms")
    elif subsystem == "MOTOR" and action == "STOP":
        _require_arg_count(subsystem, action, args, {0})
    elif subsystem == "LIGHT" and action == "MODE":
        _require_arg_count(subsystem, action, args, {1})
    elif subsystem == "SYS" and action == "HEARTBEAT":
        _require_arg_count(subsystem, action, args, {0})
