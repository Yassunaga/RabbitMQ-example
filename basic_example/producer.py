import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='fanout', routing_key='hello', body='Hello World')

channel.close()
