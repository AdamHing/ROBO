from selenium import webdriver
import pandas as pd
import time
import psutil 
import pyautogui
from datetime import datetime
import os
import argparse
import robloxpy as rpy
# d:/coding/Projects/ROBO/venv/Scripts/python.exe "d:/coding/Projects/ROBO/RobloxBots/Make-&-join/JoinGame/runbots_V3.py" acounts\BotList.csv 1234 5 AA12ISGARBAGE378


# import logging
#=========================run exe with arguments============================================================
#https://github.com/Hexcede/Roblox-Wrapper
#https://github.com/Anaminus/rbxlaunch
#=====================================================================================
# RobloxPlayerBeta.exe
#                    |
#this is mr squiggls\|/
#
#_./\./\._/(\^,,_,,^/)_./\./\./\
# Create the parser
my_parser = argparse.ArgumentParser()

# Path to the .xlsx of bot passwords and usernames
my_parser.add_argument('ListPath',metavar='ListPath',type=str,help='the path to list')
# URL for leader account
my_parser.add_argument('GameURL',metavar='GameURL',type=str,help='the url for the target game')
# The number of bot that will run
my_parser.add_argument('NumOfBots',metavar='NumOfBots',type=int,help='the num of bots to run')
# The Password for the bots
my_parser.add_argument('Password',metavar='Password',type=str,help='password for the bot accounts')

# Execute the parse_args() method
args = my_parser.parse_args()


print(args.GameURL)
print(args.ListPath)
print(args.NumOfBots)
print(args.Password)

#LogFiles
cwd = os.getcwd()
now = datetime.now()
current_time = now.strftime("%Hh%M")

options = webdriver.ChromeOptions()                 #roblox-player, RobloxPlayerBeta
prefs = {"protocol_handler": {"excluded_schemes": {"Roblox": "false"}}}
options.add_experimental_option("prefs", prefs)


#gets username and password form xlsx
try:
    dframe = pd.read_csv(args.ListPath,nrows=args.NumOfBots)

except:
    print("could not find .csv file")




names = pd.DataFrame(dframe)
print(names)

nameList = names.values.tolist()

print(nameList)
print("Wazzup my homi")

#enters username and password into roblox and goes to the game link.


for x in nameList:
    time.sleep(1)

    print(x)
 
    driver = webdriver.Chrome("C:\webdrivers\chromedriver", options=options)
    driver.get("https://www.roblox.com/login")
    time.sleep(3)
    usernameStr = x
    

    username = driver.find_element_by_id('login-username')
    username.send_keys(usernameStr)
    time.sleep(1)
    password = driver.find_element_by_id('login-password')
    password.send_keys(args.Password)
    time.sleep(2)
    signInButton = driver.find_element_by_id('login-button')
    signInButton.click()#game-details-play-button-container > button
    input()
    time.sleep(4)
    leadername = pd.DataFrame.head()
    print(leadername)
    leaderID = rpy.User.External.GetID(leadername)
    
    driver.get("https://www.roblox.com/users/{}/profile".format(leaderID))
    time.sleep(4)
    botcount = botcount + 1
    try:
        #clicks the join friend button
        JoinFriendButton = driver.find_element_by_class_name("profile-join-game")
        JoinFriendButton.click()

        #clicks the "open roblox" popup
        start = pyautogui.locateCenterOnScreen('OpenRobloxGame.PNG')
        print(start)
        if start == None:
            start = pyautogui.locateCenterOnScreen('OpenRoblox.PNG')
        time.sleep(1)
        pyautogui.moveTo(start)
        pyautogui.click(start)
        
        time.sleep(5)

    except:
        print("failed")
        break

print("All bots online.")

time.sleep(5)

#focus on window for afkness
FocusOnWin = "python " +cwd+"\WidnowFocuser\FocusOnWin.py"
psutil.Popen(FocusOnWin)