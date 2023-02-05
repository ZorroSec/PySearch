from logo import logo
from ascii import Ascii

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

Home("zorro").menu()