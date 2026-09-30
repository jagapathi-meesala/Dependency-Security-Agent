from contracts.registry import ToolRegistry
from core.validation import validate_dependency_input
from tools.dependency_audit import run


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register("dependency_audit", validate_dependency_input, run)
    return registry
