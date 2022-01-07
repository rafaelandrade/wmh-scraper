from selenium.common.exceptions import NoSuchElementException
from app.helpers.logger.console_logger import send_log
from app.helpers.error_handler.main import error_handler


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

        uses: wemake-services/wemake-python-styleguide@0.13.4
        continue-on-error: true
        with:
        Returns
            Link <str>
    """
    send_log(
        x_request_id=x_request_id,
        message=f"Getting link of a respective residence base on row "
        f"{div_number_row} and column {div_number_column}...",
    )
    try:
        link = driver.find_element_by_xpath(
            "/html/body/div[1]/main"
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
