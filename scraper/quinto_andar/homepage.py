from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants.scraper_constants_quinto_andar import quinto_andar
from events.browser.event_finish_session import finish_session
from events.browser.event_open_page import open_page
from scraper.quinto_andar.scraper_flow import scraper_flow


def verification_homepage_opened(driver) -> bool:
    """
    Function responsible for verify if homepage of QuintoAndar is open.

    Parameters:
            driver

    Return:
            <bool> True or False
    """
    state = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@class="w0f64d-0 hBSKKA"]')
        )
    )
    return bool(type(state) is str)


def homepage(x_request_id: str, driver) -> None:
    """
    Function responsible for start scraper of homepage.

    Parameters:
            x_request_id: Unique id.
            driver: Google Chrome instance.

    Returns:
            void
    """
    open_page(
        x_request_id=x_request_id,
        driver=driver,
        link=quinto_andar.get("sao_paulo"),
    )
    verification_homepage_opened(driver=driver)

    scraper_flow(x_request_id=x_request_id, driver=driver)
    finish_session(x_request_id=x_request_id, driver=driver)
