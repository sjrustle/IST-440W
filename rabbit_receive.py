import pika
from wsLogging import error_logging, audit_logging

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='FirstQ')

print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    # Set up the textfile
    try:
        note = " [x] Received %r" % (body,)
        return note
    except:
         error_logging("Rabbit Receive", "Error creating body")

def consuming_start():
    try:
        channel.basic_consume(callback,
                              queue='FirstQ',
                              no_ack=True)

        error_logging("Rabbit Receive", "Error consuming")
        channel.start_consuming()

        audit_logging("Rabbit Receive", "Able to consume")
    except:
        error_logging("Rabbit Receive", "Error starting consume")

