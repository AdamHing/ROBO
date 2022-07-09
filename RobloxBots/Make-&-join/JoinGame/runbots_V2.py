from selenium import webdriver
import pandas as pd
import time
import psutil 
import pyautogui
from datetime import datetime
import openpyxl
import os
import argparse
# import logging

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
my_parser.add_argument('LeaderURL',metavar='LeaderURL',type=str,help='the url for the leader account')
# The number of bot that will run
my_parser.add_argument('NumOfBots',metavar='NumOfBots',type=int,help='the num of bots to run')

# Execute the parse_args() method
args = my_parser.parse_args()


print(args.LeaderURL)
print(args.ListPath)
print(args.NumOfBots)#____figure out how to make it only use a certain amount of accounts____

#LogFiles
cwd = os.getcwd()
now = datetime.now()
current_time = now.strftime("%Hh%M")
LogFileSaveLocation = cwd+"\BotCountLog"

botcount = LogFileSaveLocation +r"\bot_count_"+current_time+ ".txt"
botexeptons = LogFileSaveLocation + r"\exeption_count_"+current_time+ ".txt"

f = open(botcount, "a") 
be = open(botexeptons, "a")


options = webdriver.ChromeOptions()                 #roblox-player, RobloxPlayerBeta
prefs = {"protocol_handler": {"excluded_schemes": {"Roblox": "false"}}}
options.add_experimental_option("prefs", prefs)

# driver = webdriver.Chrome('C:\webdrivers\chromedriver') 

#make sure you have a friend who is online for the bots to join

def read_excel(filename, nrows):
    # Parameter `read_only=True` leads to excel rows only being loaded as-needed
    book = openpyxl.load_workbook(filename=filename, read_only=True, data_only=True)
    first_sheet = book.worksheets[0]
    rows_generator = first_sheet.values

    header_row = next(rows_generator)
    data_rows = [row for (_, row) in zip(range(nrows - 1), rows_generator)]
    return pd.DataFrame(data_rows, columns=header_row)

# read_excel("RobloxAccounts_ S", nrows)

#os.startfile('Multiple_ROBLOX.exe') #runs program to allow multiple roblox windows

#gets username and password form xlsx
try:
    dframe = pd.read_excel(args.ListPath,nrows=args.NumOfBots)

except:
    print("could not find that .xlsx file")
    


# dframe = pd.read_excel(r'RobloxAccountsTest.xlsx')

# USAGE EXAMPLE
# dframe = read_excel('RobloxAccounts_ S.xlsx', nrows=2)

# dframe = pd.read_excel('RobloxAccounts_ S.xlsx')


names = pd.DataFrame(dframe,columns=['names'])
passwords = pd.DataFrame(dframe,columns=['passwords'])

nameList = names.values.tolist()
passwordList = passwords.values.tolist() 

print(nameList)
print('')
print(passwordList)

print("Wazzup my homi")

#enters username and password into roblox and goes to the game link.
botcount = 0
botexeptions = 0
for x,y in zip(nameList, passwordList):

    time.sleep(1)

    print(x)
    print(y)
    driver = webdriver.Chrome("C:\webdrivers\chromedriver", options=options)
    driver.get("https://www.roblox.com/login")
    time.sleep(3)
    usernameStr = x
    passwordStr = y

    username = driver.find_element_by_id('login-username')
    username.send_keys(usernameStr)
    time.sleep(1)
    password = driver.find_element_by_id('login-password')
    password.send_keys(passwordStr)
    time.sleep(2)
    signInButton = driver.find_element_by_id('login-button')
    signInButton.click()#game-details-play-button-container > button
    input()
    time.sleep(4)
    
    driver.get("https://www.roblox.com/users/177263364/profile")
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
        f.write(str(botcount)+"\n")
        time.sleep(5)

    except:
        be.write(str(botcount)+"\n")
        break
f.close()
be.close()
print("All bots online.")


time.sleep(5)

#focus on window for afkness
FocusOnWin = "python " +cwd+"\WidnowFocuser\FocusOnWin.py"
psutil.Popen(FocusOnWin)