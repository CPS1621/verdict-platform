"""
Kafka Consumer Skeleton
Week 1 - CyBreach Validator
"""

from kafka import KafkaConsumer

from config import KAFKA_BROKER
from topics import VERDICT_TOPIC


class VerdictConsumer:
    """
    Skeleton Kafka consumer for receiving verdict events.
    """

    def __init__(self):
        self.consumer = None

    def connect(self):
        """
        Connect to Kafka.
        (Implementation will be completed in Week 3)
        """
        print(f"Connecting to Kafka broker: {KAFKA_BROKER}")

    def consume(self):
        """
        Consume verdict events.
        (Implementation will be completed in Week 3)
        """
        print(f"Listening on topic: {VERDICT_TOPIC}")

    def close(self):
        """
        Close Kafka connection.
        """
        print("Closing Kafka consumer.")