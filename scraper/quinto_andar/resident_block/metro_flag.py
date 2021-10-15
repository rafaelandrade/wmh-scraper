from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep

from helpers.logger.console_logger import log


def get_metro_flag(x_request_id: str, driver) -> bool:
    """
        Function responsible for identify if has metro close to the residence.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    log(x_request_id=x_request_id, message="Searching for subway flag...")
    sleep(number=2)
    try:
        metro_flag_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[8]/div/div/span"
        )

        if metro_flag_data:
            log(
                x_request_id=x_request_id,
                message="Found information about subway...",
            )

            metro_flag_text = metro_flag_data.text

            return bool(metro_flag_text.find("Não"))
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
