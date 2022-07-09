import sys
import os
import psutil
from pathlib import Path
from time import sleep

current_dir = Path(__file__)
project_dir = str([p for p in current_dir.parents if p.parts[-1]=='ROBO'][0])

class commands(object):
    def __init__(self):
        pass
#   deploy into battle
    @staticmethod
    def exit():
        print("exiting")

    def chat(bot, message):
        
        print(bot + " " +message)
    def ToggleJumping(bool):
        # work with windows focuser
        print("test")
    


