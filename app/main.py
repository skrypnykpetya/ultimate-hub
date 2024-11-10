import uvicorn
from fastapi import FastAPI
from app.api.routers import webhook
from app.core.logging_config import setup_logging


setup_logging()

app = FastAPI()
app.include_router(webhook.router)


if __name__ == '__main__':
    uvicorn.run(app, port=8001)
