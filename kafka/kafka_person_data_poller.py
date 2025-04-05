from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'udaconnect_person_create',
    bootstrap_servers='kafka-broker:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Kafka consumer started...")

for message in consumer:
    print(f"Received message: {message.value}")