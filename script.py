import requests
from loguru import logger
from app.core.config import HOST, MONO_TOKEN
from app.main import app


def setup_webhook():
    path = app.url_path_for("webhook_mono")
    webhook_url = HOST + path

    headers = {
        "X-Token": MONO_TOKEN
    }
    body = {"webHookUrl": webhook_url}
    logger.debug(f"Body: {body}")
    url = "https://api.monobank.ua/personal/webhook"
    response = requests.post(url, data=body, headers=headers)
    logger.debug(f"Set up webhook response: {response.status_code} {response.json()}")


setup_webhook()
