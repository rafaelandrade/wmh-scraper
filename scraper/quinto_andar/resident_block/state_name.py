from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def state_name_and_district(uuid: str, driver) -> str:
    """Function responsible for get state name of building block data.

        Parameters:
                uuid: unique id
                driver: google chrome instance
    Returns:
        <str> String with state name
    """

    state_and_district = WebDriverWait(driver, 30).until\
        (EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/section[2]'
                                                   '/div[2]/div/div[1]/div[3]/div/div/a'
                                                   '/div[3]/div/p[2]')))

    return state.text if state else None
