import pika
from wsLogging import error_logging, audit_logging

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='FirstQ')


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

try:
    channel.basic_consume(callback,
                          queue='FirstQ',
                          no_ack=True)
    audit_logging("Rabbit Receive", "Basic consume")
except:
    error_logging("Rabbit Receive", "Error running CallBack")

def start_consume():
    try:
        audit_logging("Rabbit Recieve", "started consume")
        channel.start_consuming()
    except:
        error_logging("Rabbit Receive", "Error running CallBack")
