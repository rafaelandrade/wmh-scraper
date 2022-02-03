import re

from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep
from app.utils.veritification_string_has_digit import (
    verification_string_has_digit,
)

from app.helpers.logger.console_logger import send_log


def get_residence_id(x_request_id: str, driver: any) -> int:
    """
    Function responsible for return id of residence.

    Parameters:
            x_request_id: unique id
            driver: google chrome instance
    Returns:
        int
    """
    send_log(
        x_request_id=x_request_id, message="Searching for the residence id..."
    )
    sleep(number=2)
    try:
        residence_id = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/nav/ol/li[5]/a"
        )

        if residence_id:
            send_log(
                x_request_id=x_request_id,
                message=f"Found id of residence... {residence_id.text}",
            )

            residence_id_text = residence_id.text

            # Start verification if has digit
            # then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", residence_id_text)[0])
                if verification_string_has_digit(
                    x_request_id=x_request_id, text=residence_id_text
                )
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
