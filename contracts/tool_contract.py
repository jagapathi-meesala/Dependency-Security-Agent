from dataclasses import dataclass
from typing import Any, Callable, Mapping

@dataclass(frozen=True)
class ToolContract:
    name: str
    purpose: str
    input_schema: Mapping[str, Any]
    output_expectations: Mapping[str, Any]
    validator: Callable[[Any], None]
    executor: Callable[[Any], Any]
