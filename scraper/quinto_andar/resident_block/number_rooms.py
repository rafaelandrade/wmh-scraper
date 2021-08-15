import re

from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep
from utils.veritification_string_has_digit import verification_string_has_digit


def number_of_rooms(uuid: str, driver) -> int:
    """
        Function responsible for return number of rooms.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    print("Procurando pela numero de quartos")
    sleep(number=2)
    try:
        print("começando emmm....")
        number_rooms_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[2]/div/div"
        )

        if number_rooms_data:
            print(f"{uuid} - Encontrado info sobre numero de quartos")

            number_rooms = number_rooms_data.text

            # Start verification if has digit then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", number_rooms)[0])
                if verification_string_has_digit(uuid=uuid, text=number_rooms)
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
