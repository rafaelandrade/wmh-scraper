import re

from selenium.common.exceptions import NoSuchElementException

from helpers.error_handler.main import error_handler
from utils.sleep import sleep

from helpers.logger.console_logger import log


def get_rent_values(x_request_id: str, driver) -> dict:
    """
        Function responsible for get all values about the rent of the residence.

        Parameters:
                x_request_id: unique id
                driver: google chrome instance
    Returns:
        dict
    """
    log(
        x_request_id=x_request_id,
        message="Searching for a values of the rent...",
    )
    try:
        sleep(number=2)
        rent_values_data = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main/section/div/div[2]/section/div/ul"
        )

        if rent_values_data:
            log(x_request_id=x_request_id, message="Found the values...")

            rent_values_dict = {
                "rent_without_taxes": int,
                "condominium_tax": int,
                "house_tax": int,
                "fire_insurance": int,
                "service_tax": int,
                "total_rent_value": int,
            }

            rent_values = rent_values_data.text
            rent_values = rent_values.replace("Incluso", "0")
            rent_values = re.findall(r"(?<![.,])\d+[,.]{0,1}\d*", rent_values)

            # Going to get values in case of find 6 numbers in array.
            if len(rent_values) == 6:
                rent_values_dict["rent_without_taxes"] = rent_values[0]
                rent_values_dict["condominium_tax"] = rent_values[1]
                rent_values_dict["house_tax"] = rent_values[2]
                rent_values_dict["fire_insurance"] = rent_values[3]
                rent_values_dict["service_tax"] = rent_values[4]
                rent_values_dict["total_rent_value"] = rent_values[5]

            return rent_values_dict
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
