import json


def validate_message_data(uuid: str, message) -> dict:
    """
    Function responsible for validate message data.

    Parameters:
        uuid: id unique
        message: object

    Returns:
        object
    """
    print(f"{uuid} - Going to validate msg data")
    message = json.loads(message)

    return message if message.get("events") else None
