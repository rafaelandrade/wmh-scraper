from app.scraper import (
    get_number_bathrooms,
)


def test_number_bathrooms_with_5_as_number_of_bathrooms():
    """Should return 5 in case of find a text with 5 as number of bathrooms"""

    class TestHandler:
        text = "5 banheiros"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_number_bathrooms(x_request_id="", driver=driver)
    assert result == 5
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
    result = get_number_bathrooms(x_request_id="", driver=driver)
    assert result == 0
