class ChatRoomMediator:
    def show_message(self, user, message):
        pass

class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.name}]: {message}")

class User:
    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator

    def send_message(self, message):
        self.chat_mediator.show_message(self, message)

    def receive_message(self, message):
        print(f"{self.name} received: {message}")


def main():
    chat_room = ChatRoom()

    john = User("Alex", chat_room)
    jane = User("Martin", chat_room)

    while True:
        sender = input("Who is sending the message? (Alex/Martin/Exit): ")
        if sender.lower() == 'exit':
            break

        message = input("Enter message: ")

        if sender.lower() == 'alex':
            john.send_message(message)
        elif sender.lower() == 'martin':
            jane.send_message(message)
        else:
            print("Invalid sender. Please choose 'Alex' or 'Martin'.")


if __name__ == "__main__":
    main()