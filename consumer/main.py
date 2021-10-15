from helpers.error_handler.main import error_handler

from events.consumer.receive_messages import receive_messages
from events.consumer.delete_message import delete_message
from consumer.consumer_message_handler import consumer_message_handler
from helpers.request_identificator_handler.request_handler import (
    request_handler,
)
from helpers.logger.console_logger import log


def main(driver: any, queue: any) -> None:
    """
    Consumer responsible for receive messages from SQS Queue

    Parameters:
        driver: any
        queue: any

    Returns:
        None
    """
    try:
        while True:
            messages = receive_messages(queue=queue, max_number=1, wait_time=0)
            if len(messages) == 0:
                log(x_request_id="", message="Waiting messages...")
            else:
                for message in messages:
                    x_request_id = request_handler(message=message)
                    consumer_message_handler(
                        message=message,
                        x_request_id=x_request_id,
                        driver=driver,
                    )
                    delete_message(x_request_id=x_request_id, message=message)
    except AttributeError as exception:
        error_handler(exception=exception)
