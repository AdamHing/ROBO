import os
import psutil
from pathlib import Path
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import asyncio

current_dir = Path(__file__)
project_dir = str([p for p in current_dir.parents if p.parts[-1]=='ROBO'][0])



# class commands(object):
#     def __init__(self):
#         pass
# #   deploy into battle
#     @staticmethod
#     def exit():
#         print("exiting")

#     def chat(bot, message):
        
#         print(bot + " " +message)
#     def ToggleJumping(bool):
#         # work with windows focuser
#         print("test")

class Commands:

    def poplot():
        objects = []
        count = []
        for file in os.listdir("acounts"):
            if file.endswith(".csv"):
                print(file)
                df = pd.read_csv("acounts/" + file)
                count.append(len(df.index))
                
                objects.append(file)


        print(objects)
        print(tuple(objects))
        
        y_pos = np.arange(len(objects))
       
        plt.bar(y_pos, count, align='center', alpha=1)
        plt.xticks(y_pos, objects)
        plt.ylabel('Num of bots')
        plt.title('Squad population')
        plt.show()
        
    
    def test2(a):
        return a

