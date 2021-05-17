

def finish_session(uuid: str, driver) -> None:
	"""Function responsible for finish a respective session.

	Parameters:
		 uuid: Unique id.
		 driver: Google Chrome instance.

	Returns:
		void
	"""

	driver.quit()
