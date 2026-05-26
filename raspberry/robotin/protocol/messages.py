from __future__ import annotations


def _fmt(value: float) -> str:
    return f"{value:g}"


def face_expr(name: str) -> str:
    return f"FACE EXPR {name}"


def face_look(direction: str) -> str:
    return f"FACE LOOK {direction}"


def face_mouth(state: str) -> str:
    return f"FACE MOUTH {state}"


def face_blink() -> str:
    return "FACE BLINK"


def face_sleep() -> str:
    return "FACE SLEEP"


def face_wake() -> str:
    return "FACE WAKE"


def face_status() -> str:
    return "FACE STATUS"


def head_look(pan_deg: float, tilt_deg: float) -> str:
    return f"HEAD LOOK {_fmt(pan_deg)} {_fmt(tilt_deg)}"


def head_gesture(name: str) -> str:
    return f"HEAD GESTURE {name}"


def motor_drive(left: float, right: float, duration_ms: int | None = None) -> str:
    base = f"MOTOR DRIVE {_fmt(left)} {_fmt(right)}"
    if duration_ms is None:
        return base
    return f"{base} {duration_ms}"


def motor_stop() -> str:
    return "MOTOR STOP"


def light_mode(name: str) -> str:
    return f"LIGHT MODE {name}"


def heartbeat() -> str:
    return "SYS HEARTBEAT"


def build_face_expression(name: str) -> str:
    return face_expr(name)


def build_face_look(direction: str) -> str:
    return face_look(direction)


def build_face_blink() -> str:
    return face_blink()


def build_face_sleep() -> str:
    return face_sleep()


def build_face_wake() -> str:
    return face_wake()


def build_face_status() -> str:
    return face_status()


def build_heartbeat() -> str:
    return heartbeat()


def build_motor_stop() -> str:
    return motor_stop()


def build_light_mode(name: str) -> str:
    return light_mode(name)
