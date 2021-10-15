from selenium.webdriver.common.keys import Keys
from helpers.logger.console_logger import log


def event_switch_window(main_window, driver) -> classmethod:
    """
    Function responsible for switch to main windows in Chrome instance.

    Parameters:
        main_window:
        driver:

    Returns:
        void
    """
    return driver.switch_to_window(main_window)


def event_switch_right_window(x_request_id: str, driver) -> None:
    """
    Function responsible for switch to the right window.

    Parameters:
        x_request_id: str
        driver: Google Chrome instance

    Returns:
        void
    """
    log(x_request_id=x_request_id, message="Changing to the next tab...")
    driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.TAB)
