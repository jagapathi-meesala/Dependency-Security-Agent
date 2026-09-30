"""Portable adapter registry."""
from __future__ import annotations
from typing import Any
from .portable_adapter import PortableAdapter


class AdapterRegistry:
    def __init__(self) -> None:
        self._adapters: dict[str, PortableAdapter] = {}

    def register(self, adapter: PortableAdapter) -> None:
        if not adapter.name or not adapter.name.strip():
            raise ValueError("adapter name must be non-empty")
        if adapter.name in self._adapters:
            raise ValueError(f"adapter already registered: {adapter.name}")
        self._adapters[adapter.name] = adapter

    def discover(self) -> list[str]:
        return sorted(self._adapters)

    def invoke(self, name: str, payload: dict[str, Any]) -> dict[str, Any]:
        adapter = self._adapters.get(name)
        if adapter is None:
            raise KeyError(f"unknown adapter: {name}")
        return adapter.invoke(payload)
