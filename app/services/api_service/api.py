import requests
import json

from app.helpers.error_handler.main import error_handler
from app.helpers.logger.console_logger import send_log


def api_integration(
    x_request_id: str, url: str, token: str, body: dict
) -> json:
    """
    Function responsible for send request
        based on path and data body.

    Parameters:
        x_request_id: str
        url: str
        token: str
        body: dict

    """
    headers = {"Content-Type": "application/json", "Authorization": token}
    try:
        send_log(
            x_request_id=x_request_id,
            message=f"Sending request to follow path: {url} with follow data: {body}",
        )
        data = requests.post(
            url=url, data=json.dumps(body), headers=headers, timeout=25
        )
        send_log(
            x_request_id=x_request_id,
            message=f"Request finish with status: {data.status_code}",
        )
        return data
    except (
        requests.exceptions.Timeout,
        requests.exceptions.ReadTimeout,
    ) as exception:
        return error_handler(
            x_request_id=x_request_id,
            _msg="Exception occurred in api service.",
            exception=exception,
        )
