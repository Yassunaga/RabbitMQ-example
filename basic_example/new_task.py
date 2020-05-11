import sys
import pika

message = ' '.join(sys.argv[1:]) or 'Hello Wolrd!'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=message)

print(" [x] Sent %r" % message)

channel.close()
