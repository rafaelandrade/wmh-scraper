from helpers.logger.console_logger import log


def finish_session(x_request_id: str, driver) -> None:
    """
    Function responsible for finish a respective session.

    Parameters:
            x_request_id: Unique id.
            driver: Google Chrome instance.

    Returns:
            void
    """
    log(x_request_id=x_request_id, message="Finishing session of scraper...")
    driver.quit()
