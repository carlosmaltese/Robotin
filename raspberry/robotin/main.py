from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from robotin.ai.mock_intent_service import MockIntentService
from robotin.orchestrator.orchestrator import Orchestrator
from robotin.safety.safety_manager import SafetyManager


def _parse_scalar(value: str) -> Any:
    if value in {"null", "~"}:
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    try:
        return int(value)
    except ValueError:
        return value


def _load_yaml_fallback(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, result)]
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        key, _, raw_value = raw_line.strip().partition(":")
        value = raw_value.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if not value:
            child: dict[str, Any] = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = _parse_scalar(value)
    return result


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    try:
        import yaml  # type: ignore
    except ImportError:
        return _load_yaml_fallback(path)

    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping in {path}")
    return data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Robotin Raspberry control app")
    parser.add_argument("--simulation", action="store_true", help="Run without hardware")
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=Path(__file__).parent / "config",
        help="Directory containing robot.yaml and devices.yaml",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    mode = "simulation" if args.simulation else "hardware"
    print(f"[robotin] starting in {mode} mode")

    print("[robotin] loading configuration")
    try:
        config = {
            "robot": load_yaml(args.config_dir / "robot.yaml"),
            "devices": load_yaml(args.config_dir / "devices.yaml"),
        }
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(f"[robotin] configuration error: {exc}") from exc

    safety = SafetyManager()
    intent_service = MockIntentService()
    orchestrator = Orchestrator(
        config=config,
        safety=safety,
        simulation=args.simulation,
    )
    orchestrator.start()
    orchestrator.handle_intent(intent_service.next_intent())
    orchestrator.stop()
    print("[robotin] demo completed")


if __name__ == "__main__":
    main()
