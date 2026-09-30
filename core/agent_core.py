"""Framework-independent Dependency Security Agent core."""
from __future__ import annotations
from typing import Any
from contracts.registry import ToolRegistry


class AgentCore:
    def __init__(self, registry: ToolRegistry) -> None:
        self.registry = registry

    def capabilities(self) -> list[str]:
        return self.registry.list_tools()

    def execute(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.registry.execute(tool_name, payload)
