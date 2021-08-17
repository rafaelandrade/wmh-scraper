from scraper.quinto_andar.resident_block.type_of_residence import get_type_residence


def test_type_of_residence_returning_house():
    """Should return house as the type of house founded"""

    class TestHandler:
        text = "casa grande"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_type_residence(uuid="", driver=driver)
    assert result == "house"
    assert type(result) is str


def test_type_of_residence_returning_apartment():
    """Should return apartment as the type of house founded"""

    class TestHandler:
        text = "apartamento de dois andares"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_type_residence(uuid="", driver=driver)
    assert result == "apartment"
    assert type(result) is str
