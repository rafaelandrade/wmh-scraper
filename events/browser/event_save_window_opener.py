def save_window_opener(driver):
    """
    Function responsible for save main window.

    Parameters:
        driver: Google chrome instance

    Returns:
        void
    """
    print("salvando a tela principal")
    return driver.current_window_handle
