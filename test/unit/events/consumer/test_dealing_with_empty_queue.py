from app.events.consumer.dealing_with_empty_queue import (
    dealing_with_empty_queue,
)


def test_dealing_with_empty_queue(mocker):
    """
    Function send_message should be called
    """
    mocker_send_message = mocker.patch(
        "app.events.consumer.dealing_with_empty_queue.send_message",
        return_value=None,
    )

    assert dealing_with_empty_queue(queue="") is None
    assert mocker_send_message.call_count == 1
