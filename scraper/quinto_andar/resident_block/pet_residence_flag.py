from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep


def pet_flag(uuid: str, driver) -> bool:
    """
        Function responsible for flag if the residence can have pet or not.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    print("Procurando pela flag de pet")
    sleep(number=2)
    try:
        print("começando emmm....")
        pet_flag_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[6]/div/div/span"
        )

        if pet_flag_data:
            print(f"{uuid} - Encontrado info sobre pet")

            pet_flag_text = pet_flag_data.text

            return bool(pet_flag_text.find("Não"))
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
