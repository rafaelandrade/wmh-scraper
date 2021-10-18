from selenium.webdriver.common.keys import Keys
from helpers.logger.console_logger import log


def open_new_tab(x_request_id: str, link) -> None:
    """
    Function responsible for open new tab
        base on link

    Parameters:
        x_request_id: str
        link

    Returns:
        void
    """
    log(
        x_request_id=x_request_id,
        message="Opening new tab for the link the was get...",
    )
    link.send_keys(Keys.CONTROL + Keys.RETURN)
