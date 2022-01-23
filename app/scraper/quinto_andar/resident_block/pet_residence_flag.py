from selenium.common.exceptions import NoSuchElementException

from app.helpers.error_handler.main import error_handler
from app.utils.sleep import sleep

from app.helpers.logger.console_logger import send_log


def pet_flag(x_request_id: str, driver) -> bool:
    """
        Function responsible for flag if the residence can have pet or not.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    send_log(x_request_id=x_request_id, message="Searching for pet flag...")
    sleep(number=2)
    try:
        pet_flag_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[1]/div/div[3]/div/div[6]/div/div/span"
        )
        if pet_flag_data:
            send_log(
                x_request_id=x_request_id,
                message=f"Found information about pet flag {pet_flag_data.text}...",
            )

            pet_flag_text = pet_flag_data.text

            send_log(
                x_request_id=x_request_id,
                message=f"Pet flag informatio is {pet_flag_text}",
            )

            return not bool("Não" in pet_flag_text or "Nao" in pet_flag_text)
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
