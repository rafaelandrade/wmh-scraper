from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep

from app.helpers.logger.console_logger import send_log


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
    send_log(
        x_request_id=x_request_id, message="Searching for a furniture flag..."
    )
    sleep(number=2)
    try:
        flag_furniture_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[3]/div/div[7]/div/div/p"
        )
        if flag_furniture_data:
            send_log(
                x_request_id=x_request_id,
                message=f"Found information about furniture in "
                f"the residence {flag_furniture_data.text}...",
            )
            flag_furniture = flag_furniture_data.text
            flag_furniture = flag_furniture.lower()
            return bool("sem" not in flag_furniture)
    except (AttributeError, NoSuchElementException) as exception:
        return error_handler(x_request_id=x_request_id, exception=exception)
