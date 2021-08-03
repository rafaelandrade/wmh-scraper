from scraper.quinto_andar.scraper_flow import scraper_flow


def test_scraper_flow_in_case_of_not_return_link(mocker):
    """Should return None in case of not find any Link"""
    mocker.patch('scraper.quinto_andar.scraper_flow.get_link_of_resident_block', return_value=None)

    response = scraper_flow(uuid='', driver={})

    assert response is None
