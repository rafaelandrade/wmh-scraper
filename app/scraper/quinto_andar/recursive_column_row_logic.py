from app.events.browser_interaction.event_scroll_qa_page import (
    scroll_quinto_andar_page,
)


def recursive_column_row_logic(
    x_request_id: str,
    div_number_row: int,
    div_number_column: int,
    limit_scraper: int,
    driver,
) -> tuple:
    """
    Function responsible for deal with recursive column row scraper logic.

    Parameters:
        x_request_id: Unique id.
        div_number_row: Number of the block in row in the page
        div_number_column: Number of the block in column in page
        limit_scraper: Number responsible for define the limit of scraper to the page
        driver: Google Chrome instance

    Notes:
        The page is a matrix that was defined as 3 column and 2 rows each
            block of scraper. For scraper of quinto_andar the row start with
            number 3 and column with number 1. For these logic works it's important
            to deal with limit of scraper.

    Returns:
        void
    """
    if (limit_scraper - 1) % 3 == 0:
        # These represent number of row adding 1
        # and number of column return to 1
        scroll_quinto_andar_page(
            x_request_id=x_request_id,
            div_number_row=div_number_row,
            driver=driver,
        )
        return div_number_row + 1, 1

    # Number_row, number_column
    return div_number_row + 0, div_number_column + 1
