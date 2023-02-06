from home.logo.logo import logo
from home.ascii import clear
from colorama import Fore
line = '-' * 56


class Home:
    def __init__(self, name):
        self.name = name
    
    def menu(self):
        functions = {
            "searchs": ["Cep", "Cnpj", "Ddd", "Ip", "Yt Download", "Cotation", "Login"],
            "generators": ["Cep", "Cnpj", "cpf", "Name"]
        }
        
        print(logo)
        for c, key in enumerate(functions.keys()):
            print(f"[{c+1:^28}] {key}")
        opc = input('> ').replace("0", "")
        clear()
        print(f"{logo}")
        print(line)
        if opc == "1":
            for c, item in enumerate(functions['searchs']):
                print(f"[{c+1:^28}] {item}")
            print(line)
        elif opc == "2":
            for c, item in enumerate(functions['generators']):
                print(f"[{c+1:^28}] {item}")
            print(line)
        else:
            print(f"{Fore.RED} unidentified command")
            Home(self.name).menu()
        return opc
        
