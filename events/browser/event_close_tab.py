from selenium.webdriver.common.keys import Keys


def close_current_tab(driver) -> None:
    """
        Function responsible for close the tab that was opened.

        Parameters:
            driver: Google Chrome Instance

        Returns:
            void
    """

    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
