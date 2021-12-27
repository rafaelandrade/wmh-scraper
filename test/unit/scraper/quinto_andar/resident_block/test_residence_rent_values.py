from app.scraper.quinto_andar.resident_block.residence_rent_values import (
    get_rent_values,
)


def test_residence_rent_values_with_rent_values_in_response():
    """Should return an dictionary wit rent value inside"""

    class TestHandler:
        text = "Aluguel RS 43434.2"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_rent_values(x_request_id="", driver=driver)
    assert type(result) is dict


def test_resident_localization_data_with_none_as_response():
    """Should return None in case of not find any localization"""

    class TestHandler:
        text = None

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_rent_values(x_request_id="", driver=driver)
    assert result is None
