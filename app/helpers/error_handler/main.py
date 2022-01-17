import sentry_sdk

from app.config.config import config
from app.helpers.logger.console_logger import send_err

sentry_sdk.init(
    config.get("url_sentry"), environment=config.get("WMH-SCRAPER-ENV")
)


def error_handler(x_request_id=None, _msg=None, exception=None):
    """
    Function responsible for deal with
        error to construct a object and send to Sentry.

    Parameters:
        x_request_id: UniqueId
        _msg: Text responsible for complement the exception
        exception: Exception of error Optional[Union[BaseException]]

    Returns:
        void
    """
    sentry_sdk.set_tag("x_request_id", x_request_id)
    exception_id = sentry_sdk.capture_exception(exception, _msg)
    send_err(
        {
            "exception_id": exception_id,
            "exception": exception,
        },
        x_request_id=x_request_id,
    )

    return {
        "error": True,
        "message": f"{_msg}",
        "exception_id": exception_id,
        "x_request_id": x_request_id,
        "status_code": 500,
    }
