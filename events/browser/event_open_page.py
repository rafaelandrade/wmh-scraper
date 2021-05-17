

def open_page( uuid: str, driver, link: str) -> None:
	"""Function responsible for open a web page, base on specific Link.

	Parameters:
		 uuid: Unique id.
		 driver: Google Chrome instance.
		 link: URL of WebPage.

	Returns:
		void
	"""

	if link:
		driver.get(link)
