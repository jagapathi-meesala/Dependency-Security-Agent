"""Static readiness audit for required Agent Passport artifacts."""
from __future__ import annotations
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "agent.yaml", "SOUL.md", "README.md", "AGENTS.md", "DUTIES.md", "RULES.md",
    "EXPLAINABILITY.md", ".env.example", ".gitignore", "requirements.txt", "pytest.ini",
]
REQUIRED_DIRS = ["adapters", "config", "contracts", "core", "skills", "tools", "tests", "verification"]


def audit() -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_FILES:
        path = ROOT / name
        if not path.is_file() or not path.read_text().strip():
            errors.append(f"missing or empty file: {name}")
    for name in REQUIRED_DIRS:
        if not (ROOT / name).is_dir():
            errors.append(f"missing directory: {name}")

    manifest = yaml.safe_load((ROOT / "agent.yaml").read_text())
    if manifest.get("spec_version") != "0.1.0":
        errors.append("agent.yaml spec_version must be 0.1.0")
    if manifest.get("name") != "dependency-security-agent":
        errors.append("agent.yaml name mismatch")
    for skill in manifest.get("skills", []):
        if not (ROOT / "skills" / skill / "SKILL.md").is_file():
            errors.append(f"declared skill missing: {skill}")

    text = (ROOT / "EXPLAINABILITY.md").read_text()
    required = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]
    for heading in required:
        if text.count(heading) != 1:
            errors.append(f"required heading must occur exactly once: {heading}")
    for forbidden in ["## Inputs\n", "## Decision\n", "## Limits\n"]:
        if forbidden in text:
            errors.append(f"conflicting heading found: {forbidden.strip()}")
    for heading in required:
        start = text.index(heading) + len(heading)
        section = text[start:].split("\n## ", 1)[0]
        if len(re.findall(r"(?<=[.!?])\s+", section.strip())) < 1:
            errors.append(f"section lacks at least two complete sentences: {heading}")
    return errors


if __name__ == "__main__":
    errors = audit()
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print("readiness audit passed")
