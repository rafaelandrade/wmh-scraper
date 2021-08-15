from scraper.quinto_andar.resident_block.number_rooms import number_of_rooms


def test_number_rooms_with_2_as_number_of_rooms():
    """Should return 2 in case of find a text with 2 as number of rooms"""

    class TestHandler:
        text = "2 quartos"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = number_of_rooms(uuid="", driver=driver)
    assert result == 2
    assert type(result) == int


def test_number_rooms_with_0_rooms_find():
    """Should return 0 in case of not find any room"""

    class TestHandler:
        text = None

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = number_of_rooms(uuid="", driver=driver)
    assert result == 0
