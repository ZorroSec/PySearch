import os
import time


class Ascii:
    def __init__(self):
        pass
    
    def clear(self):
        return os.system("clear")
    
    def time(self):
        return time.sleep(0.225)