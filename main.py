import sentry_sdk

from config.config import config
from selenium import webdriver
from scraper.main import scraper_initiator
from utils.config_chrome_driver import creation_of_gc_instance
from utils.uuid_generator import uuid_generator


sentry_sdk.init(config.get("url_sentry"), environment=config.get("environment"))


def main():
    uuid = uuid_generator()
    options = creation_of_gc_instance()
    driver = webdriver.Chrome(options=options, executable_path="/Users/rafaelandrade/Downloads/chromedriver")
    scraper_initiator(uuid=uuid, driver=driver, type_scraper="quinto-andar")


if __name__ == '__main__':
    main()
