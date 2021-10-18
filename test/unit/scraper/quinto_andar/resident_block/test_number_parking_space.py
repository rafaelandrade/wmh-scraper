from scraper.quinto_andar.resident_block.number_parking_space import (
    get_number_parking_space,
)


def test_get_number_parking_space_with_1_parking_space():
    """Should return 2 in case of find a text with 2 as number of rooms"""

    class TestHandler:
        text = "1 estacionamento"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_number_parking_space(x_request_id="", driver=driver)
    assert result == 1
    assert type(result) is int


def test_get_number_parking_space_with_0_parking_space():
    """Should return 0 in case of not find any room"""

    class TestHandler:
        text = None

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_number_parking_space(x_request_id="", driver=driver)
    assert result == 0
    assert type(result) is int
