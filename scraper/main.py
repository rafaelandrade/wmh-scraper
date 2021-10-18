from scraper.quinto_andar.homepage import homepage
from helpers.error_handler.main import error_handler


def scraper_initiator(x_request_id: str, properties: str, driver: any) -> None:
    """
        Function responsible for initiate scraper.

    Parameters:
        x_request_id: unique id
        driver: google chrome instance
        properties: type of scraper that going to initiate

    Returns:
        None
    """
    try:
        if properties == "quinto-andar":
            homepage(x_request_id=x_request_id, driver=driver)
    except AttributeError as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
