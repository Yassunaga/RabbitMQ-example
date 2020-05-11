import time

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(ch, method, properties, body):
    print(method)
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue='hello', on_message_callback=callback
)

print('[*] Waiting for messages to exit press ctrl + c')

channel.start_consuming()
