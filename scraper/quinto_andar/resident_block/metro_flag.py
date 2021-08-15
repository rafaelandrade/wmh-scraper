from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep


def get_metro_flag(uuid: str, driver) -> bool:
    """
        Function responsible for identify if has metro close to the residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        Bool <True or False>
    """
    print("Procurando pela flag de metro")
    sleep(number=2)
    try:
        print("começando emmm....")
        metro_flag_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[8]/div/div/span"
        )

        if metro_flag_data:
            print(f"{uuid} - Encontrado info sobre metro")

            metro_flag_text = metro_flag_data.text

            return False if metro_flag_text.find("Não") else True
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
