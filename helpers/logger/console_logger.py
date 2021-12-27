import json
import logging

from coralogix.handlers import CoralogixLogger

from config.config import config

PRIVATE_KEY = f'{config.get("coralogix_secret_key")}'
APP_NAME = "WMH-Scraper"
SUB_SYSTEM = "WMH"

logger = logging.getLogger("Python Logger")
logger.setLevel(logging.DEBUG)

coralogix_handler = CoralogixLogger(
    private_key=PRIVATE_KEY, app_name=APP_NAME, subsystem=SUB_SYSTEM
)
logger.addHandler(coralogix_handler)


def log(message: str, x_request_id: str) -> None:
    """
    Function responsible for send log to Coralogix service.

    Parameters:
        message: json
        x_request_id: str

    Returns:
        None
    """
    if PRIVATE_KEY is not None:
        logger.info(
            json.dumps({"x_request_id": x_request_id, "message": message})
        )
    print(message)


def err(error) -> None:
    """
    Function responsible for send error to Coralogix service.

    Parameters:
        error: exception

    Returns:
        None
    """
    logger.error(error)
