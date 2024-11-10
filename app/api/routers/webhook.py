from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.models import Statement
from app.api.schemas.statement import MonoWebHookBody
from ..dependencies import get_db


router = APIRouter(tags=["Webhooks"], prefix="/webhook")


@router.get("/mono")
def webhook_mono_confirm():
    logger.debug("Confirm webhook")
    return {}


@router.post("/mono")
def webhook_mono(payload: MonoWebHookBody, db: Session = Depends(get_db)):
    logger.debug(f"Webhook Mono body: {payload}")
    try:
        instance = Statement(**payload.data.statementItem.dict())
        db.add(instance)
        db.commit()
        db.refresh(instance)
    except SQLAlchemyError as e:
        logger.error(f"Error during mono webhook: {e}")
    return {}
