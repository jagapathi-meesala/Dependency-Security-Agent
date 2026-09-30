from core.audit import audit_dependencies
from core.validation import validate_dependency_input

INPUT_SCHEMA = {
    "type": "object",
    "required": ["dependencies"],
    "properties": {
        "dependencies": {"type": "array"},
        "findings": {"type": "array"},
        "policy": {"type": "object"},
    },
}


def run(payload: dict) -> dict:
    validate_dependency_input(payload)
    return audit_dependencies(payload)
