from consumer.consumer_message_handler import consumer_message_handler


def test_consumer_message_handler(mocker):
    """
    Should be called
        validate_message_data and executor
    """
    mocker_validate_message = mocker.patch(
        "consumer.consumer_message_handler.validate_message_data",
        return_values={},
    )
    mocker_executor = mocker.patch(
        "consumer.consumer_message_handler.executor", return_values={}
    )

    assert consumer_message_handler(uuid="", message={}, driver={}) is None
    assert mocker_validate_message.call_count == 1
    assert mocker_executor.call_count == 1
