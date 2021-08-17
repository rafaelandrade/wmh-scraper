import re

from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep
from utils.veritification_string_has_digit import verification_string_has_digit


def residence_size(uuid: str, driver) -> int:
    """
        Function responsible for return the size of the residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        int: size of residence
    """
    print("Procurando pela numero de quartos")
    sleep(number=2)
    try:
        print("começando emmm....")
        size_residence_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[1]/div/div/span"
        )

        if size_residence_data:
            print(f"{uuid} - Encontrado tamanho do quarto")

            size_residence = size_residence_data.text
            # Start verification if has digit
            # then going to return. If do not have then return 0.
            return (
                int(re.findall(r"\d+", size_residence)[0])
                if verification_string_has_digit(uuid=uuid, text=size_residence)
                else 0
            )
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
