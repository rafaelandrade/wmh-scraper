import uuid


def uuid_generator() -> str:
	"""Function responsible for generate unique id.

	Returns:
		uuid: unique id.
	"""

	unique_id = uuid.uuid4()

	return str(unique_id)[:8]
