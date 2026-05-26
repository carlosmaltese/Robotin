from robotin.adapters.motor_adapter import MotorAdapter
from robotin.safety.safety_manager import SafetyManager


def test_emergency_stop_blocks_motor_drive() -> None:
    safety = SafetyManager()
    motor = MotorAdapter(name="motor", simulation=True, safety=safety)
    safety.trigger_emergency_stop("test")

    motor.drive(0.2, 0.2)

    assert motor.sent_lines == []
    assert not safety.can_move()


def test_emergency_stop_lifecycle() -> None:
    safety = SafetyManager()

    assert safety.emergency_stop is False
    assert safety.can_move() is True

    safety.trigger_emergency_stop("test")
    assert safety.emergency_stop is True
    assert safety.emergency_reason == "test"
    assert safety.can_move() is False

    safety.clear_emergency_stop()
    assert safety.emergency_stop is False
    assert safety.emergency_reason is None
    assert safety.can_move() is True


def test_motor_limits_are_validated() -> None:
    safety = SafetyManager(max_motor_power=0.5)

    try:
        safety.validate_motor_command(0.7, 0.1)
    except ValueError as exc:
        assert "outside" in str(exc)
    else:
        raise AssertionError("Expected ValueError")
