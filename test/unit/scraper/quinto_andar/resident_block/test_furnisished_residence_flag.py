from app.scraper import (
    get_furniture_flag,
)


def test_get_furniture_flag_with_true():
    """Should return true in case of an residence with furniture"""

    class TestHandler:
        text = "Com mobília"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_furniture_flag(x_request_id="", driver=driver)
    assert result is True
    assert type(result) is bool


def test_get_furniture_flag_with_false():
    """Should return False in case of an residence haven't any furniture"""

    class TestHandler:
        text = "Sem mobília"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_furniture_flag(x_request_id="", driver=driver)
    assert result is False
    assert type(result) is bool
