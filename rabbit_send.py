import pika
from wsLogging import error_logging, audit_logging

try:
    # Creates connection we can specify an ipAddress later
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    # Sets up connection
    channel = connection.channel("FirstQ")
except:
    error_logging("RabbitSend","Couldn't Create connection")

def send_to(Message):
    try:
        channel.basic_publish(exchange='',
                      routing_key="FirstQ",
                      body=Message)
        audit_logging("RabbitSend","Sent to queue")
        connection.close()
    except:
        error_logging("RabbitSend","Couldn't Send")


