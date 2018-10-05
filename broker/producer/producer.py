from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers='localhost:29092',
                            value_serializer=lambda v: str(v).encode('utf-8'))


while True:
    producer.send('kafka-python-topic', random.randint(1,999))