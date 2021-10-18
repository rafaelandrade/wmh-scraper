from scraper.quinto_andar.resident_block.residence_size import residence_size


def test_residence_size_with_93_as_response():
    """Should return 93 that represent the size in m²"""

    class TestHandler:
        text = "93 metros"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = residence_size(x_request_id="", driver=driver)
    assert result == 93
    assert type(result) is int


def test_residence_size_with_0_as_response():
    """Should return 0 in case of not find any size of the house"""

    class TestHandler:
        text = None

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = residence_size(x_request_id="", driver=driver)
    assert result == 0
    assert type(result) is int
