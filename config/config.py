from dotenv import load_dotenv
from os import environ

load_dotenv()

ENVIRONMENT = environ.get("environment") or None
config = {}


if ENVIRONMENT == "development":
	config["database_url"] = environ.get("DATABASE_URL")
	config["environment"] = "staging"
	config["url_sentry"] = environ.get("URL_SENTRY")
