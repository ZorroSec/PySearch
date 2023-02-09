import requests
from home.ascii import *
from colorama import Fore
from home.logo.logo import logo
from home import line
from home.search import search

class Commands:
    def __init__(self, name):
        self.name = name


    def cep(self):
        print(logo)
        print(line)
        cep = input(f"{Fore.LIGHTBLUE_EX} CEP {Fore.LIGHTBLACK_EX}> ")
        print(line)
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
        search(r)
        back()
        
    def ddd(self):
        print(logo)
        print(line)
        ddd = input(f"{Fore.LIGHTBLUE_EX} DDD {Fore.LIGHTBLACK_EX}> ")
        print(line)
        r = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json()
        search(r)
        back()
        
    def cnpj(self):
        print(logo)
        print(line)
        cnpj = input(f"{Fore.LIGHTBLUE_EX} CNPJ {Fore.LIGHTBLACK_EX}>")
        print(line)
        r = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}").json()
        search(r)
        back()
    
    def ip(self):
        print(logo)
        print(line)
        ip = input(f"{Fore.LIGHTBLUE_EX} IP {Fore.LIGHTBLACK_EX}>")
        print(line)
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        search(r)
        back()
    
    def cot(self):
        print(logo)
        print(line)
        cot = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL").json()
        search(cot)
        print(line)
        back()