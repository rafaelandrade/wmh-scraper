import re

from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep
from utils.veritification_string_has_digit import verification_string_has_digit


def get_number_bathrooms(uuid: str, driver) -> int:
    """
        Function responsible for return number of bathrooms in the residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        int
    """
    print("Procurando pelo numero de banheiro da casa...")
    sleep(number=2)
    try:
        print("começando....")
        number_bathrooms_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[3]/div/div/span"
        )
        if number_bathrooms_data:
            print(f"{uuid} - Encontrado quantidade de banheiros")

            number_bathrooms = number_bathrooms_data.text
            # Start verification if has digit
            # then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", number_bathrooms)[0])
                if verification_string_has_digit(
                    uuid=uuid, text=number_bathrooms
                )
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
