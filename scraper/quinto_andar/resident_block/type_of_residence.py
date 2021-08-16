from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep


def get_type_residence(uuid: str, driver) -> str:
    """
        Function responsible for return type of residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        str
    """
    print("Procurando pelo tipo de residencia")
    sleep(number=2)
    try:
        print("começando emmm....")
        type_residence_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[1]/h1"
        )

        if type_residence_data:
            print(f"{uuid} - Encontrado info sobre numero de quartos")

            type_residence = type_residence_data.text
            type_residence = type_residence.lower()
            if "casa" in type_residence:
                return "house"
            return "apartment"
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
