from typing import Any


def require_mapping(value: Any, field: str) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"{field} must be an object")
    return value


def validate_dependency_input(payload: Any) -> None:
    data = require_mapping(payload, "payload")
    dependencies = data.get("dependencies")
    if not isinstance(dependencies, list):
        raise ValueError("dependencies must be a list")
    for index, dependency in enumerate(dependencies):
        if not isinstance(dependency, dict):
            raise ValueError(f"dependencies[{index}] must be an object")
        name = dependency.get("name")
        version = dependency.get("version")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"dependencies[{index}].name must be a non-empty string")
        if not isinstance(version, str) or not version.strip():
            raise ValueError(f"dependencies[{index}].version must be a non-empty string")

    findings = data.get("findings", [])
    if not isinstance(findings, list):
        raise ValueError("findings must be a list")
    allowed = {"critical", "high", "medium", "low", "unknown"}
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            raise ValueError(f"findings[{index}] must be an object")
        severity = str(finding.get("severity", "unknown")).lower()
        if severity not in allowed:
            raise ValueError(f"findings[{index}].severity must be one of {sorted(allowed)}")
