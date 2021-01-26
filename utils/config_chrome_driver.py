from selenium import webdriver


def creation_of_gc_instance():
	"""Function responsible for creation of chrome driver instance"""
	options = webdriver.ChromeOptions()

	options.add_argument("--headless")
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-dev-sh-usage")
	options.add_argument("--window-size=1920,1080")
	options.add_argument("--disable-gpu")
	options.add_argument("--start-maximized")
	options.add_argument('--lang=en')
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)
	options.add_argument(
		"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) "
		"Chrome/71.0.3578.98 Safari/537.36")

	return options
