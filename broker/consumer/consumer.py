from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'kafka-python-topic', 
    bootstrap_servers='localhost:29092'
)

for msg in consumer:
    print (msg)