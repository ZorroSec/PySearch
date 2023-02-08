from pytube import YouTube, streams
from pytube.cli import on_progress
from colorama import Fore
import sys

    
def download():
    link = input(f"{Fore.CYAN} link >{Fore.RESET} ")
    op = input(f"do you really want to download this file? {Fore.LIGHTGREEN_EX}Y{Fore.LIGHTBLACK_EX}/{Fore.LIGHTRED_EX}N {Fore.LIGHTMAGENTA_EX}~> {Fore.RESET}")
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    if op == "y" or "Y":
        print(f"{Fore.LIGHTGREEN_EX}Downloading!!")
        ys.download()
    else:
        print(f"{Fore.LIGHTRED_EX}Exit!!")
        sys.exit()

download()