from faker import Faker

from scraper.quinto_andar.scraper_flow import scraper_flow

fake = Faker()


def test_scraper_flow_calling_recursive_scraper_logic(mocker):
    """Should return None after recursive scraper logic finished"""
    mock_scrape_logic = mocker.patch(
        "scraper.quinto_andar.scraper_flow.recursive_scraper_logic",
        return_value=None,
    )
    assert scraper_flow(x_request_id="", driver={}) is None
    assert mock_scrape_logic.call_count == 1
