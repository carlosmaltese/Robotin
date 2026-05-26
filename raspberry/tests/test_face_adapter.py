from __future__ import annotations

from robotin.adapters.face_adapter import FaceAdapter


def test_face_adapter_simulation_commands() -> None:
    adapter = FaceAdapter(name="face", simulation=True)

    adapter.heartbeat()
    adapter.status()
    adapter.set_expression("happy")
    adapter.look("center")
    adapter.blink()
    adapter.sleep()
    adapter.wake()

    assert adapter.sent_lines == [
        "SYS HEARTBEAT",
        "FACE STATUS",
        "FACE EXPR happy",
        "FACE LOOK center",
        "FACE BLINK",
        "FACE SLEEP",
        "FACE WAKE",
    ]

