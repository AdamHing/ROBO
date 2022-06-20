import pyfiglet as pyg  
import argparse
import sys
import os
import psutil
import subprocess as sp
import matplotlib as mpl
import numpy as np
from colorama import init, Fore
init(autoreset=True)



print("Make Bots  (1)")
print("Deploy bots(2)")
print()
mode = input("input: ") #run bots or make bots 

if mode =="1":
    #make bots
    print("Red text is optional and will be auto generated if left blank.")
    source = input(Fore.RED + "Custom list & passwords: ")
    source = input(Fore.RED + "Leader list or name: ")
    source = input("Number of bots: ")
    
    print("Number of bots          (1)")
    print("       (1)")




elif mode == "2":
    #deploy bots
    print("Make Bots  (2)")



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




