import re

from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep
from app.utils.veritification_string_has_digit import (
    verification_string_has_digit,
)

from app.helpers.logger.console_logger import send_log


def get_number_bathrooms(x_request_id: str, driver) -> int:
    """
    Function responsible for return number of bathrooms in the residence.

    Parameters:
            x_request_id: unique id
            driver: google chrome instance
    Returns:
        int
    """
    send_log(
        x_request_id=x_request_id,
        message="Searching for the number of bathrooms...",
    )
    sleep(number=6)
    try:
        number_bathrooms_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[3]/div/div[3]/div/div/p"
        )
        if number_bathrooms_data:
            send_log(
                x_request_id=x_request_id,
                message=f"Found information about the residence {number_bathrooms_data.text}...",
            )

            number_bathrooms = number_bathrooms_data.text
            # Start verification if has digit #
            # then going to return. If do not have then return 0. #
            return (
                int(re.findall(r"\d+", number_bathrooms)[0])
                if verification_string_has_digit(
                    x_request_id=x_request_id, text=number_bathrooms
                )
                else 0
            )
    except (AttributeError, NoSuchElementException, Exception) as exception:
        return error_handler(x_request_id=x_request_id, exception=exception)
