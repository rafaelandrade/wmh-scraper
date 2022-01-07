import json

from botocore.exceptions import ClientError

from app.utils.random_number_generator import random_number
from app.helpers.logger.console_logger import send_log
from app.helpers.error_handler.main import error_handler


def send_message(
    x_request_id: str,
    queue,
    message_body,
    message_attributes=None,
    thread_number: int = 0,
) -> None:
    """
    Send a message to an Amazon SQS queue.

    Parameters:
        x_request_id: unique id
        queue: The queue to receive the messages.
        message_body: The messages to send to the queue.
            These are simplified to contain only the message body and attributes.
        message_attributes: any
        thread_number: int
            represent the number of thread of queue.
                these is important to make QUEUE work in thread

    Returns:
    The response from SQS that contains the assigned message ID.
    """
    if not message_attributes:
        message_attributes = {}
    try:
        queue.send_message(
            MessageBody=message_body,
            MessageAttributes=message_attributes,
            MessageDeduplicationId=f"wmh_scraper_{random_number(10000)}",
            MessageGroupId=f"wmh_scraper_{thread_number}",
        )

        message_body = json.loads(message_body)

        send_log(
            message=f"Sending the follow msg to SQS QUEUE {message_body}",
            x_request_id=x_request_id,
        )
    except (ClientError, TypeError) as exception:
        error_handler(
            x_request_id=x_request_id,
            _msg=f"Send message failed: {message_body}",
            exception=exception,
        )
