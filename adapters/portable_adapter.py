from typing import Any
from tools.registry import build_registry

class PortableAdapter:
    """Framework-neutral invocation boundary."""
    def __init__(self) -> None:
        self.registry = build_registry()

    def invoke(self, tool_name: str, payload: Any) -> Any:
        return self.registry.execute(tool_name, payload)
