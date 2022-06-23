import pyfiglet as pyg  
import argparse
import sys
import os
import psutil
import subprocess as sp
import matplotlib as mpl
import numpy as np
from colorama import init, Fore
import colorama as cr

init(autoreset=True)



print("Make Bots   (1)")
print("Deploy bots (2)")
print()
mode = input("input: ") #run bots or make bots 

if mode =="1":
    #make bots
    print("Red text is optional and will be auto generated if left blank.")
    bots_source = input(Fore.RED + "Custom list & passwords: ")
    leaders_source = input(Fore.RED + "Leader list or name: ")
    cr.Back.RED
    numofbots = input( cr.Back.RED + "Number of bots: ")
    squad_size = input("Number of bots per leader: ")
    password = input("Password for each account: ")

elif mode == "2":
    #deploy bots
    squad_source = input(Fore.RED + "Souce file of squad: ")
    numofbots = input("Number of bots: ")
    targetid = input("ID of the target game: ")
    # extra commands to controll the bots once inside the game; spam chat, vote kick, lag the server, follow players, go to location, synchronized dancing ect.





mode = input("Custom list of usernames and passwords: ")

if mode == "1": 
   #run old bot maker
    print(Fore.RED + "will run the old bot maker")


elif mode == "0":
    input("bots per Squad: ") #number of boter per file
    
    print(Fore.RED + "The old Bot Maker")
    input("password: ")
    input("leader name: ")


print(Fore.RED + 'some red text')

res= pyg.figlet_format("Hello World")   
print(res)  