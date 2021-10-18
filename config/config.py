from dotenv import load_dotenv
from os import environ

load_dotenv()

ENVIRONMENT = environ.get("environment") or "development"
config = {}

if ENVIRONMENT == "development":
    # GENERAL #
    config["database_url"] = environ.get("DATABASE_URL")
    config["url_sentry"] = environ.get("URL_SENTRY")
    config["coralogix_secret_key"] = environ.get("CORALOGIX_PRIVATE_KEY")

    # AWS - ENV #
    config["aws_access_key_id"] = environ.get("AWS_ACCESS_KEY_ID")
    config["aws_secret_access_key"] = environ.get("AWS_SECRET_ACCESS_KEY")
    config["aws_region_name"] = environ.get("AWS_SECRET_REGION_NAME")

    # AWS - QUEUE #
    config["aws_queue_default"] = environ.get("AWS_QUEUE_SCRAPER_DEFAULT")
