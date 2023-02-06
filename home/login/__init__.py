from colorama import Fore

def login():
    username = input(f"{Fore.GREEN}Username > ")
    print(f"{Fore.LIGHTBLACK_EX} Ola {username}")
    with open('../../data.txt', 'w') as file:
        file.write(username)
