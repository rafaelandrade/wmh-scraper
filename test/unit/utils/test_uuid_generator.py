from utils.uuid_generator import uuid_generator


def test_uuid_generator_is_not_none():
	"""Functions testing UUID generator, that not return None"""

	uuid = uuid_generator()

	assert uuid is not None


def test_uuid_generator_is_str_type():
	"""Function testing UUID generator, that return str type."""

	uuid = uuid_generator()

	assert type(uuid) is str
