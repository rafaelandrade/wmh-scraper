from app.scraper.quinto_andar.resident_block.residence_id import (
    get_residence_id,
)


def test_number_bathrooms_with_5_as_number_of_bathrooms():
    """Should return id of residence in case of find a text with number"""

    class TestHandler:
        text = "Imóvel 2123131"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_residence_id(x_request_id="", driver=driver)
    assert result == 2123131
    assert type(result) is int


def test_number_bathrooms_with_0_bathrooms_find():
    """Should return 0 in case of not find any bathrooms"""

    class TestHandler:
        text = None

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_residence_id(x_request_id="", driver=driver)
    assert result == 0
