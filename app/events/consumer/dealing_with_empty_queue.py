import json

from botocore.exceptions import ClientError

from app.helpers.error_handler.main import error_handler
from app.events.consumer.send_message import send_message


def dealing_with_empty_queue(queue: any) -> None:
    """
    Function responsible for deal when
        SQS Queue do not have any messages.
        When these happens is going to send the
        default event.

    Parameters:
        queue: AWS SQS Queue
    Returns:
        None
    """
    try:
        data = {
            "x-request-id": "",
            "events": ["quintoAndarScraper"],
            "data": {
                "consumer_name": "default",
                "type_scraper": "quinto-andar",
            },
        }
        send_message(
            x_request_id="",
            queue=queue,
            message_body=json.dumps(data),
            message_attributes={},
        )
    except (AttributeError, ClientError) as exception:
        error_handler(
            _msg="Exception occurred in dealing_with_empty_queue",
            exception=exception,
        )
