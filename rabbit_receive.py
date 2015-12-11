import pika
from wsLogging import error_logging, audit_logging

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='FirstQ')

print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

try:
    channel.basic_consume(callback,
                          queue='FirstQ',
                          no_ack=True)
except:
    error_logging("Rabbit Receive", "Error running CallBack")

channel.start_consuming()
