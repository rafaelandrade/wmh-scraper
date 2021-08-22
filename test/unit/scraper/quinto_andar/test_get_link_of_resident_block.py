from faker import Faker

from scraper.quinto_andar.get_link_of_resident_block import (
    get_link_of_resident_block,
)

fake = Faker()


def test_get_link_of_resident_block_return_none():
    """Should return None in case of not find any link"""

    class Driver:
        def find_element_by_xpath(self, str):
            return None

    div_number_row = fake.unique.random_int()
    div_number_column = fake.unique.random_int()
    driver = Driver()
    assert (
        get_link_of_resident_block(
            uuid="",
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            driver=driver,
        )
        is None
    )


def test_get_link_of_resident_block_return_link():
    """Should return an link"""

    class TestHandler:
        text = "link"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    div_number_row = fake.unique.random_int()
    div_number_column = fake.unique.random_int()
    driver = Driver()
    assert (
        get_link_of_resident_block(
            uuid="",
            div_number_row=div_number_row,
            div_number_column=div_number_column,
            driver=driver,
        )
        is not None
    )
