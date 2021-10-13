import sentry_sdk

from config.config import config
from selenium import webdriver
from constants.queues_constants import queues
from utils.config_chrome_driver import creation_of_gc_instance
from utils.uuid_generator import uuid_generator
from concurrent.futures import ThreadPoolExecutor, wait

from consumer.consumers import consumers_object
from consumer.main import main


sentry_sdk.init(
    config.get("url_sentry"), environment=config.get("environment")
)


def thread(thread_number: int) -> None:
    """
    Responsible for each thread initiate a new
        consumer

    Parameters:
        thread_number: int

    Returns:
        None
    """
    print(f"executing thread number {thread_number}")

    uuid = uuid_generator()
    options = creation_of_gc_instance()
    driver = webdriver.Chrome(
        options=options,
        executable_path="/Users/rafaelandrade/Downloads/chromedriver",
    )

    main(uuid=uuid, driver=driver, queue=queues.get(f"{thread_number}"))


def principal() -> None:
    """
    Function responsible for have the logic of threads initiator

    Returns:
        None
    """
    futures_threads = []
    number_threads = len(consumers_object)
    with ThreadPoolExecutor(max_workers=number_threads) as executor:
        for thread_number in range(number_threads):
            futures_threads.append(executor.submit(thread, thread_number))

    wait(futures_threads)


if __name__ == "__main__":
    principal()
