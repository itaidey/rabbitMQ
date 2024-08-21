import pika

def rmq_callback(ch, method, properties, body):
    print(f"Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=rmq_callback)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()