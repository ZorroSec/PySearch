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
                Commands(None).cep("01001000")
                
    except KeyboardInterrupt:
        print("e")
        sys.exit()