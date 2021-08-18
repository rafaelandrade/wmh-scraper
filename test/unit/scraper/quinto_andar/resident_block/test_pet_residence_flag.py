from scraper.quinto_andar.resident_block.pet_residence_flag import pet_flag


def test_pet_residence_flag_with_true():
    """Should return True that represent the residence allow pet inside"""

    class TestHandler:
        text = "É permitido pet"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = pet_flag(uuid="", driver=driver)
    assert result is True
    assert type(result) is bool


def test_pet_residence_flag_with_false():
    """Should return False that represent the residence not allow pet inside"""

    class TestHandler:
        text = "Não é permitido pet"

    class Driver:
        def find_element_by_xpath(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    result = pet_flag(uuid="", driver=driver)
    assert result is False
    assert type(result) is bool
