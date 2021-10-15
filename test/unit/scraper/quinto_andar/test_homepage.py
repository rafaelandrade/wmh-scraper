from scraper.quinto_andar.homepage import homepage


def test_homepage(mocker):
    """
    Should be called the functions open_page,
        verification_homepage_opened, scraper_flow and finish_session
    """
    mocker_open_page = mocker.patch(
        "scraper.quinto_andar.homepage.open_page", return_value=None
    )
    mocker_verification_homepage_opened = mocker.patch(
        "scraper.quinto_andar.homepage.verification_homepage_opened",
        return_value=None,
    )
    mocker_scraper_flow = mocker.patch(
        "scraper.quinto_andar.homepage.scraper_flow", return_value=None
    )
    mocker_finish_session = mocker.patch(
        "scraper.quinto_andar.homepage.finish_session", return_value=None
    )

    assert homepage(x_request_id="", driver={}) is None
    assert mocker_open_page.call_count == 1
    assert mocker_verification_homepage_opened.call_count == 1
    assert mocker_scraper_flow.call_count == 1
    assert mocker_finish_session.call_count == 1
