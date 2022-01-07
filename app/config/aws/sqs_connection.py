import boto3
from app.config.config import config


def sqs_connection():
    """
    Function responsible for make connection in AWS SQS Service.

    Returns:
        sqs instance
    """
    return boto3.resource(
        "sqs",
        aws_access_key_id=config.get("aws_access_key_id"),
        aws_secret_access_key=config.get("aws_secret_access_key"),
        region_name=config.get("aws_region_name"),
    )
