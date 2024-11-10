import os
import pathlib
from dotenv import load_dotenv

load_dotenv()


def getenv(key, default=None):
    value = os.getenv(key, default)
    assert value, f"Missing '{key}' in config"
    return value


BASE_DIR = pathlib.Path(__file__).parent.parent.parent.resolve()
TEMPLATES_DIR = os.path.join(BASE_DIR, "app", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "app", "static")

# Logs
LOG_LEVEL = getenv("LOG_LEVEL", "INFO")

# Monobank
MONO_TOKEN = getenv("MONO_TOKEN")

# URLS
HOST = getenv("HOST", "http://127.0.0.1:8000").rstrip("/")

# DATABASE
DATABASE_HOST = getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = getenv("DATABASE_PORT", "3306")
DATABASE_USER = getenv("DATABASE_USER", "3306")
DATABASE_PASSWORD = getenv("DATABASE_PASSWORD", "password")
DATABASE_NAME = getenv("DATABASE_NAME", "oilguide")
DATABASE_URL = f"mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
