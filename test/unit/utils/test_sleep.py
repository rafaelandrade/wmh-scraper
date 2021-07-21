from utils.sleep import sleep


def test_sleep_function_should_return_none():
	"""Function responsible for test sleep function that should return None"""

	assert sleep(number=1) is None
