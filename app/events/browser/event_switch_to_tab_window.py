def event_switch_to_tab_window(main_window, driver) -> None:
    """
    Event responsible to switch to new tab windows to make easier to get
        all data.

    Parameters:
        main_window: id of main window
        driver: Google chrome instance

    Returns:
        void
    """
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
