from app.events.browser.event_save_window_opener import save_window_opener


def test_save_window_opener():
    """
    Should return None
        after a page is saved
    """

    class Driver:
        current_window_handle = None

    driver = Driver()
    assert save_window_opener(x_request_id="", driver=driver) is None
