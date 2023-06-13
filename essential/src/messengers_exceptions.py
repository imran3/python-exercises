from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class TooManyMessagesException(Exception):
    def __init__(self, message):
        super().__init__(f'Message "{message}" could not be added. Please clear existing messages')

class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self): pass


class SaveMessages(Messenger):
    savedMessages = []
    maxMessages = 10

    def receive(self, message):
        if len(self.savedMessages) > self.maxMessages:
            raise TooManyMessagesException(message)
        self.savedMessages.append(f'{getCurrentTime()} - {message}')

    def printMessages(self):
        for message in self.savedMessages:
            print(message)

    def deleteSavedMessages(self):
        self.savedMessages.clear()

# test run
listener = SaveMessages()
sender = Messenger([listener])

for i in range(0, 20):
    try:
        sender.send(f'This is message {i}')
    except TooManyMessagesException as e:
        listener.printMessages()
        listener.deleteSavedMessages()
        sender.send(f'This is message {i}')

listener.printMessages()