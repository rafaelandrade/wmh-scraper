from app.helpers.logger.console_logger import send_log


def verification_string_has_digit(x_request_id: str, text: str) -> bool:
    """
    Function responsible for verify if text has an digit or not.

    Parameters:
            x_request_id: unique id
            text: sentence that going to be verified

    Returns:
        bool: True or False
    """
    send_log(
        x_request_id=x_request_id, message="Verification if text has digit..."
    )
    if text is None:
        return False
    return any(map(str.isdigit, text))
