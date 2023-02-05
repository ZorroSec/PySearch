import os
import time
from colorama import Fore

def back():
    back = input(f"""
{Fore.BLACK}<<------------------->>
{Fore.GREEN}<<  {Fore.BLACK}[01]  {Fore.WHITE}Back       {Fore.GREEN}>>
{Fore.GREEN}<<  {Fore.BLACK}[02]  {Fore.WHITE}Exit       {Fore.GREEN}>>
{Fore.BLACK}<<------------------->>
{Fore.RED}> {Fore.WHITE}1""")
    if back == "2":
        exit()

def clear():
    return os.system('clear')

def time():
    return time.sleep(0.225)
