import re

from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep
from app.utils.veritification_string_has_digit import (
    verification_string_has_digit,
)

from app.helpers.logger.console_logger import send_log


def residence_size(x_request_id: str, driver) -> int:
    """
        Function responsible for return the size of the residence.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        int: size of residence
    """
    send_log(
        x_request_id=x_request_id,
        message="Searching for the number of bedrooms...",
    )
    sleep(number=2)
    try:
        size_residence_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[3]/div/div[1]/div/div/span"
        )
        if size_residence_data:
            send_log(
                x_request_id=x_request_id,
                message=f"Found information about bedrooms {size_residence_data.text}...",
            )

            size_residence = size_residence_data.text
            # Start verification if has digit
            # then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", size_residence)[0])
                if verification_string_has_digit(
                    x_request_id=x_request_id, text=size_residence
                )
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
