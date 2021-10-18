from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep

from helpers.logger.console_logger import log


def resident_localization_data(x_request_id: str, driver) -> list:
    """
        Function responsible for get all information
            about localization of specific residence.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        Object { street_name<String>, district_name<String>, state_name<String> }
    """
    log(
        x_request_id=x_request_id,
        message="Searching for address of residence...",
    )
    sleep(number=7)
    try:
        localization_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[1]/div[2]/p"
        )

        if localization_data:
            log(
                x_request_id=x_request_id,
                message="Found information about address...",
            )

            localization_data = localization_data.text
            return localization_data.split(",")
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
