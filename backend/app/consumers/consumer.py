import json
import traceback

from kafka import KafkaConsumer

from app.kafka.config import (
    KAFKA_SERVER,
    EVIDENCE_TOPIC,
    CONSUMER_GROUP
)

from app.database.database import SessionLocal
from app.services.rule_service import validate_uploaded_rule


consumer = KafkaConsumer(
    EVIDENCE_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    group_id=CONSUMER_GROUP,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


def start_consumer():

    print("=" * 50)
    print("Kafka Consumer Started")
    print(f"Listening on topic: {EVIDENCE_TOPIC}")
    print("=" * 50)

    for message in consumer:

        data = message.value

        print("\nReceived Event:")
        print(json.dumps(data, indent=4))

        db = SessionLocal()

        try:

            result = validate_uploaded_rule(
                db=db,
                rule_id=data["rule_id"],
                event=data["event"]
            )

            if result is None:
                print("Rule not found in database.")
            else:
                print("\nValidation Result:")
                print(json.dumps(result, indent=4))

        except Exception as e:

            print("\n========== ERROR ==========")
            print(str(e))
            traceback.print_exc()
            print("===========================\n")

        finally:
            db.close()


if __name__ == "__main__":
    start_consumer()