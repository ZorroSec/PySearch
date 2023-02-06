from pytube import YouTube, streams
from pytube.cli import on_progress
from colorama import Fore

class YtDownload:
    def __init__(self, link, yt, ys):
        self.link = link
        self.yt = yt
        self.ys = ys
    
    def download(self): 
        self.ys.download()
    
    def ytdownload(self):
        print(f"{Fore.GREEN}Title => {Fore.BLACK}{self.yt.title}")
        print(f"{Fore.GREEN}Downloading...")

link = "https://youtu.be/Z1GNW_woXI0"
yt = YouTube(link, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
YtDownload(link, yt, ys).ytdownload()
YtDownload(link, yt, ys).download()