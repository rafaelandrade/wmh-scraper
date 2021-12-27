from faker import Faker

from app.scraper.quinto_andar.recursive_scraper_logic import (
    recursive_scraper_logic,
)

fake = Faker()


def test_recursive_scraper_logic_with_time_lower_then_timeout(mocker):
    """Should return None and is testing the flow of modules"""
    mocker.patch("time.time", return_value=12345)
    mocker.patch(
        "scraper.quinto_andar.recursive_scraper_logic", return_value=None
    )
    mocker.patch(
        "scraper.quinto_andar.recursive_scraper_logic.get_link_of_resident_block",
        return_value=None,
    )
    mocker.patch(
        "scraper.quinto_andar.recursive_scraper_logic.sleep", return_value=None
    )
    mocker.patch(
        "scraper.quinto_andar.recursive_scraper_logic.recursive_column_row_logic",
        return_value=[1, 2],
    )
    timeout_start = 13
    div_number_row = fake.unique.random_int()
    div_number_column = fake.unique.random_int()
    limit_scraper = fake.unique.random_int()

    assert (
        recursive_scraper_logic(
            x_request_id="",
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            limit_scraper=limit_scraper,
            timeout_start=timeout_start,
            driver={},
        )
        is None
    )
