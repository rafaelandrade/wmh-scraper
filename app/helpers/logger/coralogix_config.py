import logging

from coralogix.handlers import CoralogixLogger

from app.config.config import config

PRIVATE_KEY = f'{config.get("coralogix_secret_key")}'
APP_NAME = "WMH-Scraper"
SUB_SYSTEM = "WMH"

logger = logging.getLogger("Python Logger")
logger.setLevel(logging.DEBUG)

coralogix_handler = CoralogixLogger(
    private_key=PRIVATE_KEY, app_name=APP_NAME, subsystem=SUB_SYSTEM
)
logger.addHandler(coralogix_handler)
