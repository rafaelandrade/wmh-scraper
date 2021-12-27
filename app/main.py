import sentry_sdk

from app.config.config import config
from selenium import webdriver
from app.constants.queues_constants import queues
from app.utils.config_chrome_driver import creation_of_gc_instance
from concurrent.futures import ThreadPoolExecutor, wait

from app.consumer.consumers import consumers_object
from app.consumer.main import main
from app.config.aws.sqs_connection import sqs_connection

sentry_sdk.init(
    config.get("url_sentry"), environment=config.get("environment")
)
sqs = sqs_connection()


def start(thread_number: int) -> None:
    """
    Responsible for each thread initiate a new
        consumer

    Parameters:
        thread_number: int

    Returns:
        None
    """
    options = creation_of_gc_instance()
    driver = webdriver.Chrome(
        options=options,
        executable_path="/Users/rafaelandrade/Downloads/chromedriver",
    )
    queue = queues.get(f"{thread_number}")
    queue = sqs.get_queue_by_name(QueueName=queue)
    main(driver=driver, queue=queue)


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
            futures_threads.append(executor.submit(start, thread_number))

    wait(futures_threads)
