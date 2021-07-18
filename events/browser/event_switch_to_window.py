

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

