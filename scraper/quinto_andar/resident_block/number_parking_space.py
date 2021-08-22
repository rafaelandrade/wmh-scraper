import re

from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep
from utils.veritification_string_has_digit import verification_string_has_digit


def get_number_parking_space(uuid: str, driver) -> int:
    """
    Function responsible for return number of parking space.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        int
    """
    print("procurando pelo numero de estacionamento...")
    sleep(number=2)
    try:
        print("começando....")
        number_parking_space_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[4]/div/div/span"
        )

        if number_parking_space_data:
            print(
                f"{uuid} - Encontrado quantidade de vagas de estacionamento..."
            )

            number_parking_space = number_parking_space_data.text

            # Start verification if has digit
            # then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", number_parking_space)[0])
                if verification_string_has_digit(
                    uuid=uuid, text=number_parking_space
                )
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
