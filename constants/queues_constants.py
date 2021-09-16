from config.config import config

"""
    DICTIONARY WITH ALL QUEUES BASE ON EACH THREAD
"""
queues = {"0": config.get("aws_queue_default")}
