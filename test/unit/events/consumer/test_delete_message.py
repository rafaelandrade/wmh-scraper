from events.consumer.delete_message import delete_message


def test_delete_message():
    """
    Should return None
        in case of delete message
        happens everything right
    """

    class Message:
        def delete(self):
            return {}

    message = Message()
    assert delete_message(x_request_id="", message=message) is None


def test_delete_message_error(mocker):
    """
    Should call error_handler
        in case of some error
    """
    mocker_error_handler = mocker.patch(
        "events.consumer.delete_message.error_handler", return_value=None
    )
    delete_message(x_request_id="", message={})

    assert mocker_error_handler.call_count == 1
