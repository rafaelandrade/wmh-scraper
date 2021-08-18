from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep


def resident_localization_data(uuid: str, driver) -> list:
    """
        Function responsible for get all information
            about localization of specific residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        Object { street_name<String>, district_name<String>, state_name<String> }
    """
    print("Procurando pelo endereço")
    sleep(number=2)
    try:
        print("começando emmm....")
        localization_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[1]/div[1]/p"
        )

        if localization_data:
            print(
                f"{uuid} - Encontrado as informações relacionado a localização do imovel"
            )

            localization_data = localization_data.text
            return localization_data.split(",")
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
