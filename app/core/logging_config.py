import sys
from fastapi.logger import logger as fastapi_logger
from loguru import logger
from app.core.config import LOG_LEVEL


def setup_logging():
    # Remove the default logger
    logger.remove()
    fastapi_logger.disabled = True

    log_format = (
        "<level>{time:YYYY-MM-DD HH:mm:ss}</level> | "
        "<level>{level: <8}</level> | "
        "<level>{name}:{module}:{line}</level> | "
        "<level>{message}</level>"
    )
    # Add a new logger with desired settings
    logger.add(
        "logs/core.log",  # Log file name
        rotation="1 week",  # Rotate logs weekly
        retention="1 month",  # Keep logs for 1 month
        level=LOG_LEVEL,  # Log level
        format=log_format,  # Log format,
    )
    logger.add(sys.stdout, level=LOG_LEVEL, format=log_format)


