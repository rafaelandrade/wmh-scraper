import requests
from bs4 import BeautifulSoup
from utils.config_chrome_driver import creation_of_gc_instance
from scraper.home_scraper.open_page import timeline
from constants.scraper_constants import quinto_andar_sp_url

def main():
	driver = creation_of_gc_instance()
	
	timeline(url=quinto_andar_sp_url, driver=driver)