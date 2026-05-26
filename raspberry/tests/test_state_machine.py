from robotin.orchestrator.state_machine import RobotState, RobotStateMachine


def test_state_machine_lifecycle() -> None:
    machine = RobotStateMachine()
    assert machine.state == RobotState.BOOTING

    machine.mark_ready()
    assert machine.state == RobotState.IDLE

    machine.activate()
    assert machine.state == RobotState.THINKING

    machine.speak()
    assert machine.state == RobotState.SPEAKING

    machine.shutdown()
    assert machine.state == RobotState.SHUTDOWN


def test_state_machine_exposes_minimum_states() -> None:
    assert {state.name for state in RobotState} == {
        "BOOTING",
        "IDLE",
        "LISTENING",
        "THINKING",
        "SPEAKING",
        "MOVING",
        "ERROR",
        "EMERGENCY_STOP",
        "SHUTDOWN",
    }


def test_state_machine_emergency() -> None:
    machine = RobotStateMachine()
    machine.mark_ready()
    machine.think()
    assert machine.state == RobotState.THINKING

    machine.emergency_stop()
    assert machine.state == RobotState.EMERGENCY_STOP

    machine.clear_emergency()
    assert machine.state == RobotState.IDLE


def test_state_machine_explicit_transitions() -> None:
    machine = RobotStateMachine()

    machine.mark_ready()
    assert machine.state == RobotState.IDLE

    machine.think()
    assert machine.state == RobotState.THINKING

    machine.speak()
    assert machine.state == RobotState.SPEAKING

    machine.move()
    assert machine.state == RobotState.MOVING

    machine.error()
    assert machine.state == RobotState.ERROR
