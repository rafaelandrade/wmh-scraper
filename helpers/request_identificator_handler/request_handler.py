import json

from utils.uuid_generator import uuid_generator


def request_handler(message: any) -> str:
    """
    Function responsible for handler with
        message get from consumer. If already had x_request_id
        going to return. If not going to generate new one.

    Parameters:
        message: any

    Returns:
        str
    """
    message = json.loads(message)

    if message.get("x_request_id"):
        return message.get("x_request_id")

    return uuid_generator()
