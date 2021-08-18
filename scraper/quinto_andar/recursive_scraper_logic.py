from events.browser.event_close_tab import close_current_tab
from events.browser.event_open_new_tab import open_new_tab
from events.browser.event_save_window_opener import save_window_opener
from events.browser.event_switch_to_tab_window import \
    event_switch_to_tab_window
from events.browser.event_switch_to_window import event_switch_right_window
from schemas.QuintoAndarSchema import QuintoAndarSchema
from scraper.quinto_andar.get_link_of_resident_block import \
    get_link_of_resident_block
from scraper.quinto_andar.recursive_column_row_logic import \
    recursive_column_row_logic
from scraper.quinto_andar.resident_block.main import get_resident_block_data
from utils.sleep import sleep


def recursive_scraper_logic(
    uuid: str, div_number_row: int, div_number_column: int, limit_scraper: int, driver
):
    """
        Function responsible for deal with recursive scraper logic.

    Parameters:
        uuid: Unique id.
        div_number_row: Number of the block in row in the page
        div_number_column: Number of the block in column in page
        limit_scraper: Number responsible for define the limit of scraper to the page
        driver: Google Chrome instance

    Notes:
        The function define the number of scraper that happens
            in the page until event of scroll happens. And the logic
            start again.

    Returns:
        void
    """
    if limit_scraper > 0:
        link = get_link_of_resident_block(
            uuid=uuid,
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            driver=driver,
        )

        quinto_andar_data = QuintoAndarSchema()

        if link:
            main_window = save_window_opener(driver=driver)
            open_new_tab(driver=driver, link=link)
            event_switch_right_window(driver=driver)
            sleep(6)
            event_switch_to_tab_window(main_window=main_window, driver=driver)
            print("Iniciando a coleta dos dados")
            get_resident_block_data(
                uuid=uuid, quinto_andar_data=quinto_andar_data, driver=driver
            )
            close_current_tab(driver=driver, main_window=main_window)
            print("\n\n VOLTANDO PARA A TELA PRINCIPAL ---")
            sleep(1)
            driver.switch_to_window(main_window)

        div_number_row, div_number_column = recursive_column_row_logic(
            uuid=uuid,
            div_number_column=div_number_column,
            div_number_row=div_number_row,
            limit_scraper=limit_scraper,
        )

        limit_scraper -= 1

        print(f"QUINTOOOOOO ANDARRRR \n\n\n{quinto_andar_data}")

        recursive_scraper_logic(
            uuid=uuid,
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            limit_scraper=limit_scraper,
            driver=driver,
        )
