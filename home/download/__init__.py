from pytube import Youtube, streams
from pytube.cli import on_progress
from colorama import Fore

class YtDonwload:
    def __init__(self, link, yt, ys):
        self.link = link
        self.yt = yt
        self.ys = ys
    
    def download(self): 
        self.ys.download()
    
    def ytdownload(self):
        print(f"{Fore.GREEN}Title => {Fore.BLACK}{yt.title}")
        print(f"{Fore.GREEN}Downloading...")
        YtDonwload.download()

link = "https://youtu.be/Z1GNW_woXI0"
yt = Youtube(link, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
YtDonwload(link, yt, ys).download()