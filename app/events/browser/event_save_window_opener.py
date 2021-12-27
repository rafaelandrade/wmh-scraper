from app.helpers.logger.console_logger import send_log


def save_window_opener(x_request_id: str, driver: any) -> any:
    """
    Function responsible for save main window.

    Parameters:
        x_request_id: str
        driver: Google chrome instance

    Returns:
        void
    """
    send_log(x_request_id=x_request_id, message="Saving main screen...")
    return driver.current_window_handle
