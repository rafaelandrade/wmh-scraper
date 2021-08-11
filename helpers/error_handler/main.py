import sentry_sdk

from config.config import config
sentry_sdk.init(config.get("url_sentry"), environment=config.get("environment"))


def error_handler(uuid, _msg=None, exception=None):
    """
    Function responsible for deal with
        error to construct a object and send to Sentry.

    Parameters:
        uuid: UniqueId
        _msg: Text responsible for complement the exception
        exception: Exception of error Optional[Union[BaseException]]

    Returns:
        void
    """
    return sentry_sdk.capture_exception(exception, _msg)
