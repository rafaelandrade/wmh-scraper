from events.browser.event_open_page import open_page


def test_open_page():
    """Should return a class method"""

    class Driver:
        def get(self, str):
            return None

    driver = Driver()
    assert open_page(x_request_id="", driver=driver, link="") is None
