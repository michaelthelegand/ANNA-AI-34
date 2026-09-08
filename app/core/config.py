from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_name: str = "ANNA AI"
    environment: str = os.getenv("ANNA_ENV", "development")
    log_level: str = os.getenv("ANNA_LOG_LEVEL", "INFO")
    default_language: str = os.getenv("ANNA_LANGUAGE", "English")

settings = Settings()
