from utils.random_number_generator import random_number


def test_random_number_generator_is_not_none_and_is_int_type():
	"""Function responsible for verify if return is not none and int type."""

	number = random_number(number=2)

	assert number is not None
	assert type(number) is int
