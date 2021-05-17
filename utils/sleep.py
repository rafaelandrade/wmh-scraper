import time
from utils.random_number_generator import random_number


def sleep(number: int) -> None:
	"""Function responsible for make a pause in code. Base on a integer.

	Parameters:
			number: integer number that going to pause a code for a interval of seconds.

	Returns:
		None
	"""

	time.sleep(random_number(number=number))
