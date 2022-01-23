import time

from app.events.browser.event_close_tab import close_current_tab
from app.events.browser.event_open_new_tab import open_new_tab
from app.events.browser.event_save_window_opener import save_window_opener
from app.events.browser.event_switch_to_tab_window import (
    event_switch_to_tab_window,
)
from app.events.browser.event_switch_to_window import event_switch_right_window
from app.schemas.QuintoAndarSchema import QuintoAndarSchema
from app.services.backoffice_services.create.quinto_andar.create_residence_flow import (
    creation_residence_data,
)

from app.scraper.quinto_andar.get_link_of_resident_block import (
    get_link_of_resident_block,
)
from app.scraper.quinto_andar.recursive_column_row_logic import (
    recursive_column_row_logic,
)
from app.scraper.quinto_andar.resident_block.main import (
    get_resident_block_data,
)
from app.utils.sleep import sleep

from app.helpers.logger.console_logger import send_log


def recursive_scraper_logic(
    x_request_id: str,
    div_number_row: int,
    div_number_column: int,
    limit_scraper: int,
    timeout_start,
    driver,
):
    """
        Function responsible for deal with recursive scraper logic.

    Parameters:
        x_request_id: Unique id.
        div_number_row: Number of the block in row in the page
        div_number_column: Number of the block in column in page
        limit_scraper: Number responsible for define the limit of scraper to the page
        timeout_start: The time that scraper begin
        driver: Google Chrome instance

    Notes:
        The function define the number of scraper that happens
            in the page until event of scroll happens. And the logic
            start again.

    Returns:
        void
    """
    timeout = 900

    sleep(15)

    # Scraper will happen for 15 minutes #
    if time.time() < timeout_start + timeout:
        link = get_link_of_resident_block(
            x_request_id=x_request_id,
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            driver=driver,
        )

        quinto_andar_data = QuintoAndarSchema()

        if link:
            main_window = save_window_opener(
                x_request_id=x_request_id, driver=driver
            )
            sleep(2)
            open_new_tab(x_request_id=x_request_id, link=link)
            sleep(3)
            event_switch_right_window(x_request_id=x_request_id, driver=driver)
            event_switch_to_tab_window(main_window=main_window, driver=driver)
            sleep(3)
            send_log(
                x_request_id=x_request_id,
                message="Initiation of collection of data...",
            )
            resident_data = get_resident_block_data(
                x_request_id=x_request_id,
                quinto_andar_data=quinto_andar_data,
                driver=driver,
            )
            creation_residence_data(
                x_request_id=x_request_id, residence_data=resident_data
            )
            close_current_tab(driver=driver, main_window=main_window)
            send_log(
                x_request_id=x_request_id, message="Return to main screen..."
            )
            sleep(1)
            driver.switch_to_window(main_window)

        div_number_row, div_number_column = recursive_column_row_logic(
            x_request_id=x_request_id,
            div_number_column=div_number_column,
            div_number_row=div_number_row,
            limit_scraper=limit_scraper,
            driver=driver,
        )

        send_log(
            x_request_id=x_request_id,
            message=f"Data of residence is: {quinto_andar_data}",
        )
        limit_scraper += 1

        recursive_scraper_logic(
            x_request_id=x_request_id,
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            limit_scraper=limit_scraper,
            timeout_start=timeout_start,
            driver=driver,
        )
