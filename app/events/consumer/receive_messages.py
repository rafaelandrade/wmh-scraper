from botocore.exceptions import ClientError
from app.helpers.error_handler.main import error_handler


def receive_messages(queue: any, max_number: int, wait_time: int):
    """
    Receive a batch of messages in a single request from an SQS queue.
    Parameters:
            queue: any The queue from which to receive messages
            max_number: any The maximum number of messages to receive.
                The actual number of messages received might be less.
            wait_time: any The maximum time to wait (in seconds)
                    before returning. When this number is greater
                    than zero, long polling is used.
                This can result in
                    reduced costs and fewer false empty responses.
    Returns:
            The list of Message objects received. These each contain the body
                of the message and metadata and custom attributes.
    """
    try:
        messages = queue.receive_messages(
            MessageAttributeNames=["All"],
            MaxNumberOfMessages=max_number,
            WaitTimeSeconds=wait_time,
        )
        return messages
    except ClientError as exception:
        error_handler(exception=exception)
