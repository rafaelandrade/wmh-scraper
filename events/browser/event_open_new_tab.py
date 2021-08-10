from selenium.webdriver.common.keys import Keys


def open_new_tab(driver, link):
    """
    Function responsible for open new tab

    Parameters:
        driver: Google Chrome instance
        link

    Returns:
        void
    """
    link.send_keys(Keys.CONTROL + Keys.RETURN)
