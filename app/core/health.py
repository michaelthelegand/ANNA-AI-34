from app.core.config import settings


def health_check() -> dict[str, str]:
    return {
        "app": settings.app_name,
        "environment": settings.environment,
        "status": "ok",
    }
