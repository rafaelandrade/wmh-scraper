from selenium.common.exceptions import NoSuchElementException
from helpers.logger.console_logger import log
from helpers.error_handler.main import error_handler


def get_link_of_resident_block(
    x_request_id, div_number_row: int, div_number_column: int, driver
) -> classmethod:
    """
    Function responsible for get link of one of blocks in QuintoAndar
        homepage.

        Parameters:
            x_request_id: UniqueId
            div_number_row: Number of the block in row in the page
            div_number_column: Number of the block in column in page
            driver: Google Chrome instance

        Returns
            Link <str>
    """
    log(
        x_request_id=x_request_id,
        message="Getting link of a respective residence...",
    )
    try:
        link = driver.find_element_by_xpath(
            "/html/body/div[1]/div/main"
            "/section[2]/div[2]/div"
            f"/div[1]/div[{div_number_row}]/div[{div_number_column}]/div/a"
        )
        return link if link else None
    except (AttributeError, NoSuchElementException) as exception:
        error_handler(
            x_request_id=x_request_id,
            _msg="Exception occurred get_link_of_resident_block",
            exception=exception,
        )
