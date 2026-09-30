from pathlib import Path

def test_env_not_committed():
    assert not Path(".env").exists()

def test_no_obvious_secret_literals():
    text = Path("core/audit.py").read_text() + Path("tools/dependency_audit.py").read_text()
    assert "sk-" not in text
    assert "password=" not in text.lower()
