from app.consumer.consumers import consumers_object
from app.helpers.logger.console_logger import send_log


def executor(
    x_request_id: str, consumer: str, properties: any, driver: any
) -> any:
    """
    Function responsible for execute a specific consumer
        that is declared in consumers object

    Parameters:
        x_request_id: str
        consumer: str
        properties: any
        driver: any

    Returns:
        None
    """
    if consumer in consumers_object:
        send_log(
            x_request_id=x_request_id,
            message=f"Going to execute consumer {consumer}... With follow properties {properties}",
        )
        return consumers_object.get(consumer)(
            x_request_id=x_request_id, properties=properties, driver=driver
        )

    send_log(
        x_request_id=x_request_id,
        message="Consumer object not found going to execute default...",
    )
    return consumers_object.get("default")(
        x_request_id=x_request_id, properties=properties, driver=driver
    )
