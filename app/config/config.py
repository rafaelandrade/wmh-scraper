from os import environ
from dotenv import load_dotenv

load_dotenv()

config = {}

if environ.get("WMH-SCRAPER-ENV") == "development":
    config["environment"] = environ.get("WMH-SCRAPER-ENV")

    # GENERAL #
    config["url_sentry"] = environ.get("URL_SENTRY")
    config["coralogix_secret_key"] = environ.get("CORALOGIX_PRIVATE_KEY")

    # AWS - ENV #
    config["aws_access_key_id"] = environ.get("AWS_ACCESS_KEY_ID")
    config["aws_secret_access_key"] = environ.get("AWS_SECRET_ACCESS_KEY")
    config["aws_region_name"] = environ.get("AWS_SECRET_REGION_NAME")

    # AWS - QUEUE #
    config["aws_queue_default"] = environ.get("AWS_QUEUE_SCRAPER_DEFAULT")

    # ENDPOINTS - MS #
    config["wmh_backoffice_endpoint"] = environ.get(
        "DEVELOPMENT_BACKOFFICE_ENDPOINT"
    )
    config["wmh_backoffice_token"] = environ.get(
        "DEVELOPMENT_BACKOFFICE_TOKEN"
    )

if environ.get("WMH-SCRAPER-ENV") == "production":
    config["environment"] = environ.get("WMH-SCRAPER-ENV")

    # GENERAL #
    config["url_sentry"] = environ.get("URL_SENTRY")
    config["coralogix_secret_key"] = environ.get("CORALOGIX_PRIVATE_KEY")

    # AWS - ENV #
    config["aws_access_key_id"] = environ.get("AWS_ACCESS_KEY_ID")
    config["aws_secret_access_key"] = environ.get("AWS_SECRET_ACCESS_KEY")
    config["aws_region_name"] = environ.get("AWS_SECRET_REGION_NAME")

    # AWS - QUEUE #
    config["aws_queue_default"] = environ.get("AWS_QUEUE_SCRAPER_DEFAULT")

    # ENDPOINTS - MS #
    config[
        "wmh_backoffice_endpoint"
    ] = "https://wmhbackoffice-prod.onrender.com"
    config["wmh_backoffice_token"] = environ.get("PRODUCTION_BACKOFFICE_TOKEN")
    config["token_backoffice"] = environ.get("TOKEN_BACKOFFICE")
