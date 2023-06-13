from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    # abstract method: to be implemented by any child class
    def receive(self): pass


class SaveMessages(Messenger):
    savedMessages = []

    def receive(self, message):
        self.savedMessages.append(f'{getCurrentTime()} - {message}')

    def printMessages(self):
        for message in self.savedMessages:
            print(message)

# test run
listener = SaveMessages()
sender = Messenger([listener])

sender.send('Hello, there! This is the first message')
sender.send('Oh hi! This is the second message!')
sender.send('Hola! This is the third and final message!')

listener.printMessages()