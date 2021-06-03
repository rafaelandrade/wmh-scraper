import requests
import json

from events.browser.event_open_page import open_page
from events.browser.event_finish_session import finish_session
from events.browser_interaction.event_scroll_page import scroll_page
from constants.scraper_constants_quinto_andar import quinto_andar_sp_url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utils.sleep import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from scraper.quinto_andar.resident_block.street_name import street_view


def homepage(uuid: str, driver):
	"""Function responsible for start scraper of homepage."""

	open_page(uuid=uuid, driver=driver, link=quinto_andar_sp_url)

	sleep(4)

	print("Page opened")

	state = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@class="w0f64d-0 hBSKKA"]')))

	print(state.text)

	street_view(uuid=uuid, driver=driver)

	finish_session(uuid=uuid, driver=driver)
