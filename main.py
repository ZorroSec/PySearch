import requests
import sys
from home.commands import Commands
from __init__ import menu
from home.ascii import clear, time, back
from home.logo.logo import logo
from colorama import Fore
from home.download import download

while True:
    try:
        opc = menu()
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
            elif inpt == "4":
                clear()
                Commands(None).ip()
            elif inpt == "5":
                clear()
                download()
            elif inpt == "6":
                clear()
                Commands(None).cot()                
    except KeyboardInterrupt:
        print("e")
        back()