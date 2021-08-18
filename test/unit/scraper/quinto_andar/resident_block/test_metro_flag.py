from scraper.quinto_andar.resident_block.metro_flag import get_metro_flag


def test_get_furniture_flag_with_true():
    """Should return True that represent that have metro close to the residence"""

    class TestHandler:
        text = "Possui metrô próximo"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_metro_flag(uuid="", driver=driver)
    assert result is True
    assert type(result) is bool


def test_get_furniture_flag_with_false():
    """Should return False that represent that have not metro close to the residence"""

    class TestHandler:
        text = "Não possui metro próximo"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_metro_flag(uuid="", driver=driver)
    assert result is False
    assert type(result) is bool
