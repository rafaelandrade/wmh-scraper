from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep

from helpers.logger.console_logger import log


def get_furniture_flag(x_request_id: str, driver) -> bool:
    """
    Function responsible for get flag that represent if the resident
        already have furniture.

    Parameters:
            x_request_id: unique id
            driver: google chrome instance
    Returns:
        int
    """
    log(x_request_id=x_request_id, message="Searching for a furniture flag...")
    sleep(number=2)
    try:
        flag_furniture_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[2]/div/div[7]/div/div/span"
        )
        if flag_furniture_data:
            log(
                x_request_id=x_request_id,
                message="Found information about furniture in the residence...",
            )
            flag_furniture = flag_furniture_data.text
            flag_furniture = flag_furniture.lower()
            return bool("sem" not in flag_furniture)
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
