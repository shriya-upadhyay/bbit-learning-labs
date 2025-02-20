from consumer_interface import mqConsumerInterface
import pika
import os
import json

class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key, exchange_name, queue_name) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.setupRMQConnection()
        self.channel
        self.connection

    def setupRMQConnection(self) -> None:
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

        exchange = self.channel.exchange_declare(exchange=self.exchange_name)

        self.channel.queue_bind(
        queue=self.queue_name,
        routing_key=self.routing_key,
        exchange=self.exchange_name,
        )

        self.channel.basic_consume(
        self.queue_name, on_message_callback, auto_ack=False
    )

def on_message_callback(self, channel, method_frame, header_frame, body) -> None:
    self.channel.start_consuming()
    message = json.loads(body)
    print(f"Received message: {message}")



def startConsuming(self) -> None:
    print(" [*] Waiting for messages. To exit press CTRL+C")
    self.channel.start_consuming()
    
    
def __del__(self) -> None:
    print("Closing RMQ connection on destruction")
    self.channel.close()
    self.connection.close()
