from app.core.config import settings
from app.core.health import health_check


def test_health_check():
    result = health_check()

    assert result["app"] == "ANNA AI"
    assert result["status"] == "ok"


def test_settings_app_name():
    assert settings.app_name == "ANNA AI"
