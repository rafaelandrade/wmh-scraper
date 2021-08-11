from selenium.common.exceptions import (ElementNotInteractableException,
                                        WebDriverException)

from events.browser.event_close_tab import close_current_tab
from events.browser.event_open_new_tab import open_new_tab
from events.browser.event_save_window_opener import save_window_opener
from events.browser.event_switch_to_tab_window import \
    event_switch_to_tab_window
from events.browser.event_switch_to_window import event_switch_right_window
from helpers.error_handler.main import error_handler
from scraper.quinto_andar.get_link_of_resident_block import \
    get_link_of_resident_block
from scraper.quinto_andar.resident_block.main import get_resident_block_data
from utils.sleep import sleep


def scraper_flow(uuid, driver):
    """
        Function responsible for deal with flow logic of QuintoAndar scraper.

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
            sleep(6)
            event_switch_to_tab_window(main_window=main_window, driver=driver)
            print("Iniciando a coleta dos dados")
            get_resident_block_data(uuid=uuid, driver=driver)
            close_current_tab(driver=driver, main_window=main_window)

        sleep(5)

    except (WebDriverException, ElementNotInteractableException) as exception:
        error_handler(
            uuid=uuid, _msg="Exception occurred on scraper_flow", exception=exception
        )
