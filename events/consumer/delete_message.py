from botocore.exceptions import ClientError
from helpers.error_handler.main import error_handler


def delete_message(uuid: str, message) -> None:
    """
    Delete an message from a queue.
    Parameters:
        uuid: Unique id str
        message: The message to delete. The message's queue URL is
            contained in the message's metadata.

    Returns:
        None
    """
    try:
        message.delete()
        print("Message was deleted with success.")
    except (ClientError, AttributeError) as exception:
        error_handler(uuid=uuid, exception=exception)
