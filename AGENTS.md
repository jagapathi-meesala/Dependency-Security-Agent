# Architecture

The core implementation is framework-independent Python. Tool contracts define inputs and outputs; the registry discovers and invokes tools; adapters translate external framework calls into the portable contract.

# Development Rules

Keep runtime configuration in environment variables. Keep domain rules deterministic and documented in RULES.md. Avoid framework-specific imports in core modules.

# Tool Conventions

Each tool validates its input and returns a structured result. Tool failures use explicit error objects rather than fabricated successful output.

# Testing Rules

Run `pytest -q` after implementation changes. Tests cover validation, deterministic classification, registry behavior, adapters, documentation structure, and security-related input handling.

# Portability

Adapters must depend on the portable contract rather than changing core behavior. Framework packages are optional; adapter tests verify behavior that can be tested without those external packages.
