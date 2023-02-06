import requests
import sys
from home.commands import Commands
from __init__ import Home
from home.ascii import clear, time
from home.logo.logo import logo
from colorama import Fore

while True:
    try:
        opc = Home(None).menu()
        inpt = input(f"{Fore.GREEN}> ")
        if opc == "1":
            if inpt == "1":
                clear()
                Commands(None).cep()
            elif inpt == "2":
                clear()
                Commands(None).cnpj()
            elif inpt == "3":
                clear()
                Commands(None).ddd()
    except KeyboardInterrupt:
        print("e")
        sys.exit()