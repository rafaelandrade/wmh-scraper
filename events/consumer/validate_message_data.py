import json

from helpers.logger.console_logger import log


def validate_message_data(x_request_id: str, message: any) -> dict:
    """
    Function responsible for validate message data.

    Parameters:
        x_request_id: id unique
        message: object

    Returns:
        object
    """
    log(x_request_id=x_request_id, message="Validating message...")
    message = json.loads(message)

    return message if message.get("events") else None
