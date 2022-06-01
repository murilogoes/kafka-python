from kafka import KafkaConsumer

consumer = KafkaConsumer('meutopico', bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(message)