from selenium.webdriver.common.keys import Keys


def close_current_tab(driver) -> None:
    """
        Function responsible for close the tab that was opened.

        Parameters:
            driver: Google Chrome Instance
        Returns:
            void
    """

    print("Fechando a aba aberta")
    driver.close()
