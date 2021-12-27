import json

from app.helpers.request_identificator_handler.request_handler import (
    request_handler,
)
from app.utils import uuid_generator


def test_request_handler():
    """
    Should return the same request_id
        in case an object that already has.
    """
    uuid_test = uuid_generator()
    message = {"x_request_id": uuid_test}

    assert request_handler(message=json.dumps(message)) == uuid_test


def test_request_handler_without_request_in_object(mocker):
    """
    Should create a request_id
        in case of object without request_id and uuid_generator should be called
    """
    uuid_test = "AAAAA"
    mocker_uuid_generator = mocker.patch(
        "helpers.request_identificator_handler.request_handler.uuid_generator",
        return_value=uuid_test,
    )
    message = {"potato": 1}
    assert request_handler(message=json.dumps(message)) == uuid_test
    assert mocker_uuid_generator.call_count == 1
