from scraper.quinto_andar.homepage import homepage


def scraper_initiator(uuid: str, driver, type_scraper: str) -> None:
	"""Function responsible for initiate scraper.

	Parameters:
			uuid: unique id
			driver: google chrome instance
			type_scraper: type of scraper that going to initate

	Returns:
		None
	"""
	try:
		if type_scraper == "quinto-andar":
			homepage(uuid=uuid, driver=driver)
	except Exception as exception:
		print(f"Error on scraper_initiator: {exception}", exception)
