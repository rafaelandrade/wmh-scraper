from events.browser.event_switch_to_window import (
    event_switch_window,
    event_switch_right_window,
)


def test_event_switch_window():
    """Should return a class method"""

    class TestHandler:
        text = None

    class Driver:
        def switch_to_window(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    assert event_switch_window(main_window="", driver=driver) is not None


def test_event_switch_right_window():
    """Should return a class method"""

    class TestHandler:
        def send_keys(self, str):
            return None

    class Driver:
        def find_element_by_tag_name(self, str):
            testHandler = TestHandler()
            return testHandler

    driver = Driver()
    assert event_switch_right_window(x_request_id="", driver=driver) is None
