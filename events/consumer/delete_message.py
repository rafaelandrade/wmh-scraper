from botocore.exceptions import ClientError
from helpers.error_handler.main import error_handler

from helpers.logger.console_logger import log


def delete_message(x_request_id: str, message) -> None:
    """
    Delete an message from a queue.

    Parameters:
        x_request_id: Unique id str
        message: The message to delete. The message's queue URL is
            contained in the message's metadata.

    Returns:
        None
    """
    try:
        message.delete()
        log(
            x_request_id=x_request_id,
            message="Message have been deleted with success.",
        )
    except (ClientError, AttributeError) as exception:
        error_handler(x_request_id=x_request_id, exception=exception)
