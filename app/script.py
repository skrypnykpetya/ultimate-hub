import requests
from app.core.config import HOST, MONO_TOKEN
from app.main import app


def setup_webhook():
    url = app.url_path_for("webhook_mono")
    print(url)
