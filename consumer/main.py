from helpers.error_handler.main import error_handler

from events.consumer.receive_messages import receive_messages
from consumer.consumer_message_handler import consumer_message_handler


def main(uuid: str, driver: any, queue: any) -> None:
    """"""
    try:
        while True:
            messages = receive_messages(
                uuid=uuid, queue=queue, max_number=1, wait_time=0
            )
            if len(messages) == 0:
                print("0 mensagem")
            else:
                for message in messages:
                    consumer_message_handler(
                        message=message, uuid=uuid, driver=driver
                    )
    except Exception as exception:
        error_handler(uuid=uuid, exception=exception)
