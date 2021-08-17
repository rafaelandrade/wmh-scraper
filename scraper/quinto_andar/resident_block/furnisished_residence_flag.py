from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep


def get_furniture_flag(uuid: str, driver) -> bool:
    """
    Function responsible for get flag that represent if the resident
        already have furniture.

    Parameters:
    -----------
            uuid: unique id
            driver: google chrome instance
    Returns:
        int
    """
    print("procurando se a residencia possui imóveis...")
    sleep(number=2)
    try:
        print("começando...")
        flag_furniture_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/main/section/div/div[1]/div/div[2]/div/div[7]/div/div/span"
        )
        if flag_furniture_data:
            print("encontrado algo relacionado se a casa tem imóveis")
            flag_furniture = flag_furniture_data.text
            flag_furniture = flag_furniture.lower()
            return bool(not "sem" in flag_furniture)
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(uuid=uuid, exception=exception)
