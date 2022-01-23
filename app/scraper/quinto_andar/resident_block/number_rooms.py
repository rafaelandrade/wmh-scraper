import re

from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep
from app.utils.veritification_string_has_digit import (
    verification_string_has_digit,
)

from app.helpers.logger.console_logger import send_log


def number_of_rooms(x_request_id: str, driver) -> int:
    """
        Function responsible for return number of rooms.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    send_log(
        x_request_id=x_request_id, message="Searching for number of rooms..."
    )
    sleep(number=2)
    try:
        number_rooms_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[3]/div/div[2]/div/div/p"
        )

        if number_rooms_data:
            send_log(
                x_request_id=x_request_id,
                message=f"Found information about number of rooms, {number_rooms_data.text}...",
            )

            number_rooms = number_rooms_data.text

            # Start verification if has digit
            # then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", number_rooms)[0])
                if verification_string_has_digit(
                    x_request_id=x_request_id, text=number_rooms
                )
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
