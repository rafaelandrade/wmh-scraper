import json
import logging

from coralogix.handlers import CoralogixLogger

from config.config import config

PRIVATE_KEY = config.get("coralogix_secret_key")
APP_NAME = "wmh-scraper"
SUB_SYSTEM = "where_is_my_house"

logger = logging.getLogger("Python Logger")
logger.setLevel(logging.INFO)

coralogix_handler = CoralogixLogger(PRIVATE_KEY, APP_NAME, SUB_SYSTEM)
logger.addHandler(coralogix_handler)


def log(message: json, x_request_id: str) -> None:
    if PRIVATE_KEY is not None:
        logger.info(
            json.dumps({"x_request_id": x_request_id, "message": message})
        )
    print(message)


def err(error) -> None:
    logger.error(error)
