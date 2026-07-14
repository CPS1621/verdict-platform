"""
Kafka Producer Skeleton
Week 1 - CyBreach Validator
"""

from kafka import KafkaProducer
import json

from config import KAFKA_BROKER
from topics import VERDICT_TOPIC


class VerdictProducer:
    """
    Skeleton Kafka producer for publishing verdict events.
    """

    def __init__(self):
        self.producer = None

    def connect(self):
        """
        Connect to Kafka.
        (Implementation will be completed in Week 3)
        """
        print(f"Connecting to Kafka broker: {KAFKA_BROKER}")

    def publish_verdict(self, verdict_event):
        """
        Publish a verdict event.
        (Implementation will be completed in Week 3)
        """
        print(f"Publishing to topic: {VERDICT_TOPIC}")
        print(json.dumps(verdict_event, indent=4))

    def close(self):
        """
        Close Kafka connection.
        """
        print("Closing Kafka producer.")