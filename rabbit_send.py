import pika
from wsLogging import error_logging, audit_logging

try:
    # Creates connection we can specify an ipAddress later
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    # Sets up connection
    channel = connection.channel()

    channel.queue_declare(queue='FirstQ')

    # Logs
    audit_logging("Rabbit Send", "Connected to Queue")
except:
    error_logging("RabbitSend","Couldn't Create connection")

def send_to(Message):
    try:
        channel.basic_publish(exchange='',
                      routing_key="FirstQ",
                      body=str(Message))
        #Logs process
        audit_logging("RabbitSend","Sent to queue")
        connection.close()
    except:
        # Logs Process
        error_logging("RabbitSend","Couldn't Send")


