import pika
from wsLogging import error_logging, audit_logging

def create_connection(queueName):
    try:
        # Creates connection we can specify an ipAddress later
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        # Sets up connection
        channel = connection.channel(queueName)

        return channel
    except:
        error_logging("RabbitSend","Couldn't Create connection")

def send_to(qName,Message):
    try:
        channel = create_connection(qName)
        channel.basic_publish(exchange='',
                      routing_key=qName,
                      body=Message)
        audit_logging("RabbitSend","Sent to queue")
    except:
        error_logging("RabbitSend","Couldn't Send")


