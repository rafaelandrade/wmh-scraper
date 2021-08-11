from utils.sleep import sleep
from helpers.error_handler.main import error_handler
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from events.browser_interaction.event_scroll_page import scroll_page


def resident_localization_data(uuid: str, driver):
    """
        Function responsible for get all information about localization of specific residence.

        Parameters:
        -----------
                uuid: unique id
                driver: google chrome instance
    Returns:
        Object { street_name<String>, district_name<String>, state_name<String> }
    """
    sleep(15)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    sleep(2)
    print(soup)
    print("Procurando pelo endereço")
    try:
        print("começando emmm....")
        localization_data = driver.find_element_by_xpath('//*[@id="app"]/div/div/main/section/div/div[1]/div/div[1]/div[1]/p')

        if localization_data:
            print(f"{uuid} - Encontrado as informações relacionado a localização do imovel")

            print(localization_data)
            print(localization_data.text)
    except Exception as exception:
        error_handler(uuid=uuid, exception=exception)
