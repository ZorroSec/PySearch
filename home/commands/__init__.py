import requests
from home.ascii import *
from colorama import Fore

class Commands:
    def __init__(self, name):
        self.name = name

    def search(r):
        for key, value in r.items():
            print(f"{Fore.BLUE}{key} {Fore.WHITE}=> {Fore.RED}{value} ")

    def cep(self, cep):
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
        Commands.search(r)
        back()
    def ddd(self, ddd):
        return {}
    
