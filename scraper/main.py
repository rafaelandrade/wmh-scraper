from scraper.quinto_andar.homepage import homepage
from helpers.error_handler.main import error_handler


def scraper_initiator(uuid: str, properties: str, driver: any) -> None:
    """
        Function responsible for initiate scraper.

    Parameters:
        uuid: unique id
        driver: google chrome instance
        properties: type of scraper that going to initiate

    Returns:
        None
    """
    try:
        if properties == "quinto-andar":
            homepage(uuid=uuid, driver=driver)
    except AttributeError as exception:
        error_handler(uuid=uuid, exception=exception)
