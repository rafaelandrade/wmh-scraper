from selenium.webdriver.common.keys import Keys


def close_current_tab(driver, main_window) -> None:
    """
        Function responsible for close the tab that was opened.

        Parameters:
            driver: Google Chrome Instance
            main_window: Id of homepage window
        Returns:
            void
    """

    print("Fechando a aba aberta")
    screens = driver.window_handles
    new_screen_id = [screen for screen in screens if screen != main_window][0]
    driver.switch_to.window(new_screen_id)
    driver.close()
