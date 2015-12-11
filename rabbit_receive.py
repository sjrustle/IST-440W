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

def start_consuming():
    try:
        channel.basic_consume(callback,
                              queue='FirstQ',
                              no_ack=True)

        error_logging("Rabbit Receive", "Error consuming")
        channel.start_consuming()

        audit_logging("Rabbit Recieve", "Able to consume")
    except:
        error_logging("Rabbit Recieve", "Error starting consume")

