from typing import Any, Callable

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, tuple[Callable[[Any], None], Callable[[Any], Any]]] = {}

    def register(self, name: str, validator: Callable[[Any], None], executor: Callable[[Any], Any]) -> None:
        if not name or name in self._tools:
            raise ValueError("tool name must be unique and non-empty")
        self._tools[name] = (validator, executor)

    def discover(self) -> list[str]:
        return sorted(self._tools)

    def execute(self, name: str, payload: Any) -> Any:
        if name not in self._tools:
            raise KeyError(f"unknown tool: {name}")
        validator, executor = self._tools[name]
        validator(payload)
        return executor(payload)
