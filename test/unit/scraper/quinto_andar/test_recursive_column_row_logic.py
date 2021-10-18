from faker import Faker

from scraper.quinto_andar.recursive_column_row_logic import (
    recursive_column_row_logic,
)

fake = Faker()


def test_recursive_column_row_logic_with_div_number_column_plus_1():
    """Should return div_number_column + 1
    with limit_scraper not being one number more
    then a number divisible by 3. That represents
    that in the scraper flow not going to
    next row.
    """
    div_number_column = fake.unique.random_int()
    div_number_row = fake.unique.random_int()
    limit_scraper = 2
    response = recursive_column_row_logic(
        x_request_id="",
        div_number_row=div_number_row,
        div_number_column=div_number_column,
        limit_scraper=limit_scraper,
        driver={},
    )
    assert response is not None
    assert response[0] == div_number_row
    assert response[1] == div_number_column + 1


def test_recursive_column_row_logic_with_div_number_row_plus_1(mocker):
    """Should return div_number_row + 1
    and div_number_column going to be 1
    with limit_scraper being one number more
    then a number divisible by 3. That represents
    that in the scraper flow going to
    next row of residences.
    """
    mocker.patch(
        "scraper.quinto_andar.recursive_column_row_logic.scroll_quinto_andar_page",
        return_value=None,
    )
    div_number_column = fake.unique.random_int()
    div_number_row = fake.unique.random_int()
    limit_scraper = 4
    response = recursive_column_row_logic(
        x_request_id="",
        div_number_row=div_number_row,
        div_number_column=div_number_column,
        limit_scraper=limit_scraper,
        driver={},
    )
    assert response is not None
    assert response[0] == div_number_row + 1
    assert response[1] == 1
