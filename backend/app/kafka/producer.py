import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = None

try:
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    print("✅ Connected to Kafka")
except Exception as e:
    print(f"⚠️ Kafka is not available: {e}")


def publish_verdict(verdict: dict):
    if producer:
        try:
            producer.send("verdict-events", verdict)
            producer.flush()
            print("✅ Verdict published to Kafka")
        except KafkaError as e:
            print(f"❌ Failed to publish verdict: {e}")
    else:
        print("⚠️ Kafka producer not initialized. Skipping publish.")

def publish_corrected_verdict(verdict: dict):
    """
    Publish a corrected verdict event to Kafka.
    """

    if producer:
        try:
            producer.send("verdict-events", verdict)
            producer.flush()
            print("✅ Corrected verdict published to Kafka")
        except KafkaError as e:
            print(f"❌ Failed to publish corrected verdict: {e}")
    else:
        print("⚠️ Kafka producer not initialized.")