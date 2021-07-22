from utils.sleep import sleep

from scraper.quinto_andar.get_link_of_resident_block import get_link_of_resident_block
from events.browser.event_save_window_opener import save_window_opener
from events.browser.event_open_new_tab import open_new_tab
from events.browser.event_switch_to_window import event_switch_right_window
from events.browser.event_close_tab import close_current_tab
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import WebDriverException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC


def scraper_flow(uuid, driver):
    """Function responsible for deal with flow logic of QuintoAndar scraper.

    Parameters:
        uuid: Unique id.
        driver: Google Chrome instance

    Returns:
        void
    """

    try:
        print("Iniciando o fluxo de scraper")
        link = get_link_of_resident_block(uuid=uuid, driver=driver)

        if link:
            main_window = save_window_opener(driver=driver)
            open_new_tab(driver=driver, link=link)
            event_switch_right_window(driver=driver)
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            close_current_tab(driver=driver, main_window=main_window)

    except (WebDriverException, ElementNotInteractableException) as exception:
        print(exception)
