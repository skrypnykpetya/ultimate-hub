import json
from typing import Any

from fastapi import APIRouter, Request, Body
from loguru import logger


router = APIRouter(tags=["Webhooks"], prefix="/webhook")


@router.get("/mono")
def webhook_mono_confirm():
    logger.debug("Confirm webhook")
    return {}


@router.post("/mono")
def webhook_mono(request: Request, payload: Any = Body(None)):
    logger.debug(payload)
    return {}
