author = ’Sadaf’

!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters (host= “localhost’))

channel = connection.channel()

channel.queue_declare(queue= ‘IST’)

channel.basic_publish(exchange=‘’, routing_key=‘this’, body= ’This is IST 440 W’ )

print “ [x] Sent ’This is IST 440 W’ “ connection.close()
