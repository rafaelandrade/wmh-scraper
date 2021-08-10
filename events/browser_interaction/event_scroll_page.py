from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


def scroll_page(self, uuid: str, number_scrolls: int, driver) -> None:
	"""Function responsible for make scroll in page.

	Parameters:
		self
		uuid: Unique Id.
		number_scrolls: integer number that represent many times that going to make scroll.
		driver: google chrome instance

	Returns:
		None
	"""
	print(uuid)

	try:
		for _ in range(number_scrolls):
			driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
	except ElementClickInterceptedException as exception:
		self.print(f"Exception occured on scroll page. Error: {exception}", exception)
