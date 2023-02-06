from colorama import Fore

class Login:
    def __init__(self, name):
        self.name = name
    
    def writeData(self, name):
        with open('data.txt', 'w') as file:
            file.write(name)