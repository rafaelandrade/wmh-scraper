import secrets


def random_number(number: int) -> int:
	"""Function responsible for generator a random number.

	Parameters:
		number: integer number that represent the max number that going to
			generate the random number.
	"""

	return secrets.choice([1, number])
