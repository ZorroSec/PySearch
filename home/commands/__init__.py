import requests
from ascii import *
class Commands:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def search(r):
        for key, value in r.items():
            print(f"{az}{key} {br}=> {vm}{value} ")

    def cep(self, cep):
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
        Commands.search(r)
    
