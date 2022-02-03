import sentry_sdk

from app.config.config import config
from selenium import webdriver
from app.constants.queues_constants import queues
from app.utils.config_chrome_driver import creation_of_gc_instance
from concurrent.futures import ThreadPoolExecutor, wait

from app.consumer.consumers import consumers_object
from app.consumer.main import main
from app.config.aws.sqs_connection import sqs_connection
from app.helpers.logger.console_logger import send_log

sentry_sdk.init(
    config.get("url_sentry"), environment=config.get("WMH-SCRAPER-ENV")
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
    driver = webdriver.Chrome(options=options)
    queue = queues.get(f"{thread_number}")
    queue = sqs.get_queue_by_name(QueueName=queue)
    send_log(
        message=f"Initiation of WMH-Scraper with environment {config.get('environment')}...",
        x_request_id="",
    )
    send_log(
        message=f"BACKOFICE{config.get('token_backoffice')} "
        f"- AND TEST2 {config.get('wmh_backoffice_token')}",
        x_request_id="",
    )

    send_log(
        message=f"ENDPOINT {config.get('wmh_backoffice_endpoint')}",
        x_request_id="",
    )

    send_log(
        message=f"SENTRY {config.get('url_sentry')}",
        x_request_id="",
    )

    send_log(
        message=f"AWS REGION {config.get('aws_region_name')}",
        x_request_id="",
    )
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
