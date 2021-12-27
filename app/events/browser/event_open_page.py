from app.helpers.logger.console_logger import send_log


def open_page(x_request_id: str, driver, link: str) -> None:
    """Function responsible for open a web page, base on specific Link.

    Parameters:
            x_request_id: Unique id.
            driver: Google Chrome instance.
            link: URL of WebPage.

    Returns:
            void
    """
    if link:
        driver.get(link)

    send_log(
        x_request_id=x_request_id,
        message=f"Page was open with follow link {link}...",
    )
