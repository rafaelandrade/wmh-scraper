from events.browser.event_finish_session import finish_session


def test_finish_session():
    """
    Should return
        void after a session
        is finished
    """

    class Driver:
        def quit(self):
            return {}

    driver = Driver()

    assert finish_session(uuid="", driver=driver) is None
