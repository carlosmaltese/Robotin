from __future__ import annotations

from robotin import main as robotin_main


def test_simulation_boot_runs_without_hardware(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["robotin.main", "--simulation"],
    )

    robotin_main.main()

    output = capsys.readouterr().out
    assert "[robotin] starting in simulation mode" in output
    assert "[robotin] loading configuration" in output
    assert "[robotin] orchestrator started" in output
    assert "[face] FACE EXPR happy" in output
    assert "[face] FACE LOOK center" in output
    assert "[face] FACE MOUTH talking" in output
    assert "[light] LIGHT MODE warm" in output
    assert "[head] HEAD GESTURE small_nod" in output
    assert "[voice] Hola, soy Robotin." in output
    assert "[robotin] demo completed" in output
