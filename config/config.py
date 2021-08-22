from dotenv import load_dotenv
from os import environ

load_dotenv()

ENVIRONMENT = environ.get("environment") or "development"
config = {}


if ENVIRONMENT == "development":
    config["database_url"] = environ.get("DATABASE_URL")
    config["url_sentry"] = environ.get("URL_SENTRY")
