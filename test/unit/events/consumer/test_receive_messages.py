from app.events.consumer.receive_messages import receive_messages


def test_receive_messages():
    """
    Should not return None
    """

    class Queue:
        def receive_messages(
            self, MessageAttributeNames, MaxNumberOfMessages, WaitTimeSeconds
        ):
            return {}

    queue = Queue()

    assert receive_messages(queue=queue, max_number=1, wait_time=2) is not None
