from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def scroll_page(uuid: str, number_scrolls: int, driver) -> None:
    """Function responsible for make scroll in page.

    Parameters:
            uuid: Unique Id.
            number_scrolls: integer number that represent many times that going to make scroll.
            driver: google chrome instance

    Returns:
            None
    """
    print(uuid)
    print("SCROOOLLL")
    import time

    try:
        time.sleep(10)
        element = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section[2]/div[2]/div/div[1]/div[6]"
        )

        if element:
            print("dENTROOOOO DO SCROLLL")
            actions = ActionChains(driver)
            actions.move_to_element(element)
            # perform the operation on the element
            actions.perform()
    except ElementClickInterceptedException as exception:
        print(f"Exception occured on scroll page. Error: {exception}", exception)
