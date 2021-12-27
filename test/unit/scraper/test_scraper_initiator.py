from app.scraper.main import scraper_initiator


def test_scraper_initiator(mocker):
    """
    Should called quinto andar initiator
    """
    mocker_homepage = mocker.patch("scraper.main.homepage", return_value=None)

    assert (
        scraper_initiator(
            x_request_id="", properties="quinto-andar", driver={}
        )
        is None
    )
    assert mocker_homepage.call_count == 1
