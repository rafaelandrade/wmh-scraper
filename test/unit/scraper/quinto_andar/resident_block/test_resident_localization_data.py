from scraper.quinto_andar.resident_block.resident_localization_data import resident_localization_data


def test_resident_localization_data_with_localization_as_response():
    """Should return an array with 3 as the length with localization data inside"""

    class TestHandler:
        text = "Rua São Paulo, Bairro Ribeirinha, São Paulo"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = resident_localization_data(uuid="", driver=driver)
    assert type(result) is list


def test_resident_localization_data_with_none_as_response():
    """Should return None in case of not find any localization"""

    class TestHandler:
        text = None

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = resident_localization_data(uuid="", driver=driver)
    assert result is None
