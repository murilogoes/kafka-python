from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

producer.send('meutopico', b'Hello, World!')
producer.send('meutopico', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
