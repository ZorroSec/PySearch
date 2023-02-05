from home.logo.logo import logo
from home.ascii import clear

line = '-' * 56


class Home:
    def __init__(self, name):
        self.name = name
    
    def menu(self):
        functions = {
            "searchs": ["Cep", "Cnpj", "Ip", "Yt Download"],
            "generators": ["Cep", "Cnpj", "cpf", "Name"]
        }
        
        print(logo)
        for c, key in enumerate(functions.keys()):
            print(f"[{c+1}] {key}")
        opc = input('> ')
        clear()
        print(f"{logo}")
        print(line)
        
