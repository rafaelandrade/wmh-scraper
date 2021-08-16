from scraper.quinto_andar.resident_block.furnisished_residence_flag import \
    get_furniture_flag


def test_get_furniture_flag_with_true():
    """Should return true in case of an residence with furniture"""

    class TestHandler:
        text = "Com mobília"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = get_furniture_flag(uuid="", driver=driver)
    assert result is True
    assert type(result) is bool
