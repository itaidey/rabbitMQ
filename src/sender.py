import pika

class Sender:
    def __init__(self, queue_name: str='hello', address: str='localhost' ) -> None:
        self.queue = queue_name
        self.address = address
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

    def send_message(self, message: str):
        try:
            self.channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body=message)
        except Exception as e:
            print(f"Error sending message {message}")

    def __del__(self) -> None:
        print("running sender del")
        self.channel.close()


def main():

    sender = Sender(queue_name='hello', address='localhost')
    while True:
        try:
            message = input("Insert the message to send:")
            sender.send_message(message)
        except Exception as e:
            exit()

if __name__=='__main__':
    main()
