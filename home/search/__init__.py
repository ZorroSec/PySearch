from colorama import Fore

def search(r):
    for key, value in r.items():
        print(f"{Fore.BLUE}{key} {Fore.WHITE}=> {Fore.RED}{value} ")