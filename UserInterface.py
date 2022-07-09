import pyfiglet as pyg  
import argparse
import sys
import os
from subprocess import *
from colorama import init, Fore,Style
from pathlib import Path


#run(["start", "/wait", "cmd", "/K", "echo test", "arg /?\^"], shell=True)


os.system("start /B start cmd.exe @cmd /k {'echo test'}")
init(autoreset=True)


current_dir = Path(__file__)
project_dir = str([p for p in current_dir.parents if p.parts[-1]=='ROBO'][0])

print(project_dir)
print("Make Bots   (1)")
print("Deploy bots (2)")
print()

x =1
while x == 1:
    x = 0
    mode = input("input: ") #run bots or make bots 
    if mode =="1":
        #make bots
        print("Red text is optional and will be auto generated if left blank.")
        bots_source = input(Fore.RED + "Custom list & passwords: ")
        
        print(Style.RESET_ALL)
        if not(bots_source and leaders_source):
            leaders_source = input("Leader ID: ")
            squad_size = input("Number of bots per squade recomended 16: ")
            numofbots = input("Number of bots: ")
            
            
            password = input("Password for each account: ")

            runmode = input("Run mode: ")
#=================open new window here
        c = 'python project_dir/RobloxBots/Make-&-join/BotMaker/SemiAutoBotMaker.py', leaders_source, numofbots, password,runmode,squad_size
        # os.system("start /wait cmd /k {c}")

        #os.system("start /B start cmd.exe @cmd /k {dir}"

    elif mode == "2":
        #deploy bots
        squad_source = input(Fore.RED + "Souce file of squad: ")
        numofbots = input("Number of bots: ")
        targetid = input("ID of the target game: ")
        # extra commands to controll the bots once inside the game; spam chat, vote kick, lag the server, follow players, go to location, synchronized dancing ect.

    else:
        x = 1
        print("not valid")



print(Fore.RED + 'some red text')

res= pyg.figlet_format("Hello World")   
print(res)