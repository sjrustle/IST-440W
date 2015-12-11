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
        file_body = body.split()
        _file = open("RabbitMq", "w")
        _file.write(file_body)
        _file.close()
        return body
    except:
         error_logging("Rabbit Receive", "Error creating body")


try:
    channel.basic_consume(callback,
                          queue='FirstQ',
                          no_ack=True)
    audit_logging("Rabbit Receive", "Was able to receive")
except:
    error_logging("Rabbit Receive", "Error consuming")

def start_consuming():
    channel.start_consuming()
