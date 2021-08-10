from selenium.webdriver.common.keys import Keys


def event_switch_window(main_window, driver) -> None:
    """
    Function responsible for switch to main windows in Chrome instance.

    Parameters:
        main_window:
        driver:

    Returns:
        void
    """
    return driver.switch_to_window(main_window)


def event_switch_right_window(driver):
    """
    Function responsible for switch to the right window.

    Parameters:
            driver: Google Chrome instance

    Returns:
        void
    """
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
