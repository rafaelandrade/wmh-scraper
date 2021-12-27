from app.helpers.error_handler.main import error_handler

from app.events.consumer.receive_messages import receive_messages
from app.events.consumer.delete_message import delete_message
from app.consumer.consumer_message_handler import consumer_message_handler
from app.helpers.request_identificator_handler.request_handler import (
    request_handler,
)
from app.helpers.logger.console_logger import send_log
from app.events.consumer.dealing_with_empty_queue import (
    dealing_with_empty_queue,
)

from app.utils.sleep import sleep


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
                send_log(
                    x_request_id="",
                    message="QUEUE with 0 messages, going to send default event in 15 minutes...",
                )
                sleep(number=900)
                dealing_with_empty_queue(queue=queue)
            else:
                for message in messages:
                    x_request_id = request_handler(message=message.body)
                    send_log(
                        x_request_id=x_request_id,
                        message="Receive message going to start scraper flow...",
                    )
                    consumer_message_handler(
                        message=message.body,
                        x_request_id=x_request_id,
                        driver=driver,
                    )
                    delete_message(x_request_id=x_request_id, message=message)
    except AttributeError as exception:
        error_handler(exception=exception)
