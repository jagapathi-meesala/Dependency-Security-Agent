"""Environment-backed runtime configuration."""
from __future__ import annotations
import os


class ConfigurationError(ValueError):
    """Raised when required runtime configuration is missing or invalid."""


def required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or not value.strip():
        raise ConfigurationError(f"Required environment variable {name} is missing")
    return value.strip()


def load_settings() -> dict[str, str]:
    """Load only explicitly configured runtime values; no production defaults."""
    return {
        "environment": required_env("DEPENDENCY_SECURITY_ENVIRONMENT"),
        "log_level": required_env("DEPENDENCY_SECURITY_LOG_LEVEL"),
    }
