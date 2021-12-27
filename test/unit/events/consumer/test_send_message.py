import json
from app.events.consumer.send_message import send_message


def test_send_message():
    """
    Should return None
    """

    class Queue:
        def send_message(
            self,
            MessageBody,
            MessageAttributes,
            MessageDeduplicationId,
            MessageGroupId,
        ):
            return None

    queue_mock = Queue()

    assert (
        send_message(
            x_request_id="",
            queue=queue_mock,
            message_body=json.dumps({"data": "test"}),
        )
        is None
    )


def test_send_message_error(mocker):
    """
    Should called error_handler in case
        of some error occurred
    """
    mocker_error_handler = mocker.patch(
        "events.consumer.send_message.error_handler", return_value=None
    )

    class Queue:
        def send_message(
            self,
            MessageBody,
            MessageAttributes,
            MessageDeduplicationId,
            MessageGroupId,
        ):
            return None

    queue_mock = Queue()

    send_message(
        x_request_id="",
        queue=queue_mock,
        message_body={"data": "test"} is None,
    )
    assert mocker_error_handler.call_count == 1
