from consumer.consumers import consumers_object


def executor(uuid: str, consumer: str, properties: any, driver: any) -> None:
    """
    aaa

    Parameters:
        uuid: str
        consumer: str
        properties: any
        driver: any

    Returns:
        None
    """

    if consumer in consumers_object:
        print(
            f"Going to execute consumer {consumer}... With follow properties {properties}"
        )
        return consumers_object.get(consumer)(
            uuid=uuid, properties=properties, driver=driver
        )
    else:
        print("consumer object not found going to execute the default")
        return consumers_object.get("default")(
            uuid=uuid, properties=properties, driver=driver
        )
