import json

from app.events.consumer.validate_message_data import validate_message_data


def test_validate_message():
    """
    Should return same object in case of
        message have events in object
    """
    data = {"events": "test"}
    response = validate_message_data(
        x_request_id="str", message=json.dumps(data)
    )
    assert response == data


def test_validate_message_without_events():
    """
    Should return None in case of message
        without events in object
    """
    data = {}
    response = validate_message_data(
        x_request_id="str", message=json.dumps(data)
    )

    assert response is None
