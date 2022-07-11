import pyfiglet as pyg  
import subprocess
from colorama import init, Fore,Style
from pathlib import Path
import psutil
import RobloxBots.support.commands as commands
import asyncio

#will display a pyplot of the squads
#commands.commandstwo.poplot()


init(autoreset=True)


current_dir = Path(__file__)
project_dir = str([p for p in current_dir.parents if p.parts[-1]=='ROBO'][0])

print(project_dir)
print("Make Bots   (1)")
print("Deploy bots (2)")
print()


x = 1
while x == 1:
    x = 0
    mode = input("input: ") #run bots or make bots 
    if mode =="1":
        #make bots
        print("Red text is optional and will be auto generated if left blank.")
        bots_source = input(Fore.RED + "Custom list & passwords: ")
        
        print(Style.RESET_ALL)
        if not(bots_source and leaderId):
            leaderId = input("Leader ID: ")
            squad_size = input("Number of bots per squade recomended 16: ")
            numofbots = input("Number of bots: ")
            
            password = input("Password for each account: ")
            runmode = input("Run mode: ")
#=================open new window here
        botMaker = project_dir + '/venv/Scripts/python.exe ' +'"'+project_dir + r'\RobloxBots\Make-&-join\BotMaker\SemiAutoBotMaker.py'+'"'+" "+ leaderId+ " "+numofbots+ " "+password + " "+runmode+ " "+squad_size
        print(botMaker)
        
        subprocess.Popen(botMaker)
       


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

#some kind of comand thing



while True:
    cmd = input("> ")
    #some thing like this 
    # output = commands.commandstwo
    #print(output)
