import json
import requests

from app.helpers.logger.coralogix_config import (
    PRIVATE_KEY,
    SUB_SYSTEM,
    APP_NAME,
)


def get_body_coralogix(severity: int, message: str, x_request_id: str) -> dict:
    """
    Function responsible for return the body to send
        to coralogix:

    Parameters:
        severity: int
        message: str
        x_request_id: str

    Returns:
        dict
    """
    return {
        "privateKey": PRIVATE_KEY,
        "applicationName": APP_NAME,
        "subsystemName": SUB_SYSTEM,
        "computerName": APP_NAME,
        "logEntries": [
            {
                "severity": severity,
                "text": json.dumps(
                    {"message": message, "x_request_id": x_request_id}
                ),
            }
        ],
    }


def send_log(message: str, x_request_id: str):
    """
    Function responsible for send log to Coralogix service.

    Parameters:
        message: json
        x_request_id: str

    Returns:
        None
    """
    body = get_body_coralogix(
        severity=3, message=message, x_request_id=x_request_id
    )
    headers = {"Content-Type": "application/json"}
    if PRIVATE_KEY is not None:
        requests.post(
            url="https://api.coralogix.com/api/v1/logs",
            headers=headers,
            data=json.dumps(body),
        )
    print(message)


def send_err(error: any, x_request_id: str) -> None:
    """
    Function responsible for send error to Coralogix service.

    Parameters:
        error: exception
        x_request_id: str

    Returns:
        None
    """
    body = get_body_coralogix(
        severity=5, message=error, x_request_id=x_request_id
    )
    headers = {"Content-Type": "application/json"}
    if PRIVATE_KEY is not None:
        requests.post(
            url="https://api.coralogix.com/api/v1/logs",
            headers=headers,
            data=json.dumps(body),
        )
    print(error)
