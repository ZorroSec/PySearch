from colorama import Fore
from home.logo import logo

def login():
    print(logo)
    username = input(f"{Fore.GREEN}Username > ")
    print(f"{Fore.LIGHTBLACK_EX} Ola {username}")
    with open('../../data.txt', 'w') as file:
        file.write(username)
