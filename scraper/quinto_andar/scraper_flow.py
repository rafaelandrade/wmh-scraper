import time
from selenium.common.exceptions import (ElementNotInteractableException,
                                        WebDriverException)

from constants.scraper_constants_quinto_andar import quinto_andar
from helpers.error_handler.main import error_handler
from scraper.quinto_andar.recursive_scraper_logic import \
    recursive_scraper_logic
from utils.sleep import sleep


def scraper_flow(uuid, driver):
    """
        Function responsible for deal with flow logic of QuintoAndar scraper.

    Parameters:
        uuid: Unique id.
        driver: Google Chrome instance

    Returns:
        void
    """
    try:
        timeout_start = time.time()
        print(f"Iniciando o fluxo de scraper as {timeout_start}")
        recursive_scraper_logic(
            uuid=uuid,
            div_number_row=quinto_andar["div_number_row_initiator"],
            div_number_column=quinto_andar["div_number_column_initiator"],
            limit_scraper=quinto_andar["limit_scraper"],
            timeout_start=timeout_start,
            driver=driver,
        )
        sleep(10)
        print("\n\nTERMINOOOOOOOOU")
    except (WebDriverException, ElementNotInteractableException) as exception:
        error_handler(
            uuid=uuid, _msg="Exception occurred on scraper_flow", exception=exception
        )
