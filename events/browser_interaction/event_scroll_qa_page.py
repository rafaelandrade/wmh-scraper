from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from helpers.error_handler.main import error_handler
from utils.sleep import sleep


def scroll_quinto_andar_page(
    x_request_id: str, div_number_row: int, driver
) -> None:
    """
    Function responsible for make scroll in quinto andar page
        base on below divs.

    Parameters:
            x_request_id: Unique Id.
            div_number_row: Number of the block in row in the page
            driver: google chrome instance

    Returns:
            None
    """
    try:
        element = driver.find_element_by_xpath(
            f"/html/body/div[1]/main/section[2]/div[2]/div/div[1]/div[{div_number_row+2}]"
        )
        sleep(number=3)
        if element:
            actions = ActionChains(driver)
            actions.move_to_element(element)
            actions.perform()
    except (ElementClickInterceptedException, AttributeError) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
