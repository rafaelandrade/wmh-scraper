from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def street_view(uuid: str, driver):
    """Function responsible for initiate scraper.

        Parameters:
                uuid: unique id
                driver: google chrome instance

    Returns:
        None
    """

    street = WebDriverWait(driver, 30).until\
        (EC.presence_of_element_located((By.XPATH, '/html/body/div[1]'
                                                   '/div/main/section[2]'
                                                   '/div[2]/div/div[1]/div[2]'
                                                   '/div[1]/div/a/div[3]/div/p[1]')))
    print(street.text)

    teste = WebDriverWait(driver, 30).until\
        (EC.presence_of_element_located((By.XPATH, '/html/body/div[1]'
                                                   '/div/main/section[2]'
                                                   '/div[2]/div/div[1]/div[2]/div[2]')))

    print(teste.text)
    return
