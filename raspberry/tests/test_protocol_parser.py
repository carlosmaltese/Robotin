import pytest

from robotin.protocol.messages import (
    build_face_blink,
    build_face_expression,
    build_face_look,
    build_face_sleep,
    build_face_status,
    build_face_wake,
    build_heartbeat,
    build_light_mode,
    build_motor_stop,
)
from robotin.protocol.parser import parse_line


@pytest.mark.parametrize(
    ("line", "target", "command", "args"),
    [
        ("FACE EXPR happy", "FACE", "EXPR", ("happy",)),
        ("FACE EXPR angry", "FACE", "EXPR", ("angry",)),
        ("FACE EXPR curious", "FACE", "EXPR", ("curious",)),
        ("FACE LOOK left", "FACE", "LOOK", ("left",)),
        ("FACE LOOK up", "FACE", "LOOK", ("up",)),
        ("FACE LOOK down", "FACE", "LOOK", ("down",)),
        ("FACE BLINK", "FACE", "BLINK", ()),
        ("FACE STATUS", "FACE", "STATUS", ()),
        ("FACE SLEEP", "FACE", "SLEEP", ()),
        ("FACE WAKE", "FACE", "WAKE", ()),
        ("FACE MOUTH talking", "FACE", "MOUTH", ("talking",)),
        ("HEAD LOOK 15 -5", "HEAD", "LOOK", ("15", "-5")),
        ("MOTOR DRIVE 0.2 0.2", "MOTOR", "DRIVE", ("0.2", "0.2")),
        ("MOTOR STOP", "MOTOR", "STOP", ()),
        ("LIGHT MODE thinking", "LIGHT", "MODE", ("thinking",)),
        ("SYS HEARTBEAT", "SYS", "HEARTBEAT", ()),
    ],
)
def test_parse_known_commands(
    line: str, target: str, command: str, args: tuple[str, ...]
) -> None:
    parsed = parse_line(line)

    assert parsed.target == target
    assert parsed.command == command
    assert parsed.subsystem == target
    assert parsed.action == command
    assert parsed.args == args


def test_command_builders() -> None:
    assert build_face_expression("happy") == "FACE EXPR happy"
    assert build_face_look("center") == "FACE LOOK center"
    assert build_face_blink() == "FACE BLINK"
    assert build_face_sleep() == "FACE SLEEP"
    assert build_face_wake() == "FACE WAKE"
    assert build_face_status() == "FACE STATUS"
    assert build_heartbeat() == "SYS HEARTBEAT"
    assert build_motor_stop() == "MOTOR STOP"
    assert build_light_mode("warm") == "LIGHT MODE warm"


@pytest.mark.parametrize(
    "line",
    [
        "",
        "FACE DANCE fast",
        "FACE EXPR",
        "FACE BLINK now",
        "FACE STATUS now",
        "FACE SLEEP now",
        "FACE WAKE now",
        "HEAD LOOK 15 nope",
        "HEAD LOOK 15",
        "MOTOR DRIVE fast 0.2",
        "MOTOR DRIVE 0.2 0.2 long",
        "MOTOR STOP now",
        "LIGHT MODE",
        "SYS HEARTBEAT now",
    ],
)
def test_rejects_invalid_commands(line: str) -> None:
    with pytest.raises(ValueError):
        parse_line(line)
