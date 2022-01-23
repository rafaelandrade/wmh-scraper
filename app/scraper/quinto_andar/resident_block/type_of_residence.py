from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep

from app.helpers.logger.console_logger import send_log


def get_type_residence(x_request_id: str, driver) -> str:
    """
        Function responsible for return type of residence.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        str
    """
    send_log(
        x_request_id=x_request_id,
        message="Searching for the type of residence...",
    )
    sleep(number=2)
    try:
        type_residence_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[2]/div[1]/h1"
        )
        if type_residence_data:
            send_log(
                x_request_id=x_request_id,
                message=f"Found the type of residence {type_residence_data.text}...",
            )

            type_residence = type_residence_data.text
            type_residence = type_residence.lower()
            if "casa" in type_residence:
                return "house"
            return "apartment"
    except (AttributeError, NoSuchElementException) as exception:
        return error_handler(x_request_id=x_request_id, exception=exception)
