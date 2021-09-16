from helpers.error_handler.main import error_handler
from events.consumer.validate_message_data import validate_message_data
from consumer.executor import executor


def consumer_message_handler(uuid: str, message: any, driver: any) -> None:
    """"""
    try:
        data = validate_message_data(uuid=uuid, message=message)
        executor(
            uuid=uuid,
            consumer=data.get("data").get("consumer_name"),
            properties=data.get("data").get("type_scraper"),
            driver=driver,
        )
    except Exception as exception:
        error_handler(uuid=uuid, exception=exception)
