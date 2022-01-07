import requests_mock
from app.services.api_service.api import api_integration


def test_api_integration(mocker):
    """
    Should return status 200 of request
    """
    mocker.patch("app.services.api_service.api.send_log", return_value="None")
    with requests_mock.Mocker() as mock:
        mock.post("http://0.0.0.0:3333", text="test")
        data = api_integration(
            x_request_id="", url="http://0.0.0.0:3333", token="", body={}
        )
        assert data.status_code == 200
