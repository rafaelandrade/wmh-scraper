from faker import Faker

from utils.veritification_string_has_digit import verification_string_has_digit

faker = Faker()


def test_verification_string_has_digit_should_return_true():
    """Should return True in case of have digit in text"""
    text = "1batata"
    response = verification_string_has_digit(x_request_id="", text=text)
    assert response is True
    assert type(response) is bool


def test_verification_string_has_digit_should_return_false():
    "Should return False in case of not have any digit in text"
    text = "batata"
    response = verification_string_has_digit(x_request_id="", text=text)
    assert response is False
    assert type(response) is bool


def test_verification_string_has_digit_should_return_false_in_case_of_none():
    "Should return False in case of text is None"
    text = None
    response = verification_string_has_digit(x_request_id="", text=text)
    assert response is False
    assert type(response) is bool
