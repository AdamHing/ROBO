from sys import int_info
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import argparse
import string
import random
import robloxpy as rpy
import os
import csv
import pandas as pd
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#& d:/coding/Projects/ROBO/venv/Scripts/python.exe "d:/coding/Projects/ROBO/RobloxBots/Make-&-join/Bot_managing/BotMaker/SemiAutoBotMaker.py" 177263364 3 AA12ISGARBAGE378 


#use right after making so you dont have to save

#root dir of project
current_dir = Path(__file__)
project_dir = str([p for p in current_dir.parents if p.parts[-1]=='ROBO'][0])

dir_path = os.path.dirname(os.path.realpath(__file__))

my_parser = argparse.ArgumentParser()
# URL for leader account
my_parser.add_argument('LeaderID',metavar='LeaderID',type=str,help='the ID of the leader account')
# The number of bot that will run
my_parser.add_argument('NumOfBots',metavar='NumOfBots',type=int,help='the num of bots to run')
#password that all the accounts will use
my_parser.add_argument('Password',metavar='Password',type=str,help='password that all the accounts will use')
# URL for leader account
my_parser.add_argument('Mode',metavar='Mode',type=int,help='testing mode(0) or working mode(1)')
# Execute the parse_args() method
args = my_parser.parse_args()

print(args.LeaderID)
print(args.NumOfBots)
print(args.Password)
print(args.Mode)

#python Package\BotMaker\SemiAutoBotMaker.py https://www.roblox.com/users/177263364/profile 5 R "Password"

#===============================b-day vars=============================
bdaymonth='February'
bdayday='02'
bdayyear='2005'
#==========================random valid name generator==========================("valid" = filterout bad substrings)

blacklist = []
#takes words out of csv and puts them into a single list.
with open(dir_path+ r"\bad-words3.csv", newline='') as inputfile:
    for row in csv.reader(inputfile):
        blacklist.append(row[0])

invalid = 0
#random str generator
N = 18    # name length
C = 16    #bots per squad
overflowfile =project_dir +"\\acounts"+"\\overflow"+".csv"# path var

for i in range(args.NumOfBots):
    # gererate random name
    name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))
    # name = input("name: ")
    if rpy.User.External.DoesNameExist(name) == "Unavailible":
        invalid = invalid+1
        print(name + " is invalid: already taken")
    #underscore filtering
    elif (name[:1] == "_" or name[-1] == "_" or name.count('_') > 1):
        invalid = invalid+1
        print(name + " is invalid: underscore")
    #substring filtering
    elif any(word in name for word in blacklist):
        invalid = invalid+1
        print(name + " is invalid: on blacklist")
    else:
        print("worked")
        #print valid names to csv file
        # f = open(dir_path+r'\valid-names.csv','a')
        # f.write(name+'\n') 
   
    # f.close()
    print(name)
#===========================use names to make bots=========================================


#enters username and password into roblox and goes to the game link.

    time.sleep(1)
    
    #driver = webdriver.Chrome(str(project_dir)+r'\RobloxBots\Settings&Config\WebDriver\chromedriver.exe')
    print("heeeooeo")
    print(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://www.roblox.com/")
    time.sleep(2)
    
    username = driver.find_element_by_id('signup-username')
    password = driver.find_element_by_id('signup-password')
    signInButton = driver.find_element_by_id('signup-button')
    # gender = driver.find_element_by_id(sex+"Button")
    month = driver.find_element_by_id("MonthDropdown")
    day = driver.find_element_by_id("DayDropdown")
    year = driver.find_element_by_id("YearDropdown")
    #BDAY:
    #//*[@id="MonthDropdown"]
    select = Select(month)
    select.select_by_visible_text(bdaymonth)
    # select.select_by_value(bdaymonth)

    select = Select(day)
    select.select_by_value(bdayday)

    select = Select(year)
    select.select_by_value(bdayyear)

    username.send_keys(name)
    
    time.sleep(1)
    
#===============Sends friend request to leader=====================================
    if args.Mode==1:
        ValidationOutput = driver.find_element_by_id("signup-usernameInputValidation").text
        if ValidationOutput:
            print(name)
            print("Username cannot be used")
            print("Reason:", ValidationOutput)
    else:
        #store valid and verified roblox bot names.

        if not (os.path.exists(overflowfile)):
            myfile = open(overflowfile,'w')
            myfile.close()
            print("first loop thing")
        
        with open(overflowfile,'a') as fd:
            fd.write(name+"\n")
            fd.close()
            df = pd.read_csv(overflowfile)
            print(df[df.columns[0]].count())

        # with open(str(project_dir)+r'\accounts'+'\BotList.csv','a') as fd:
        #     fd.write("\n"+ name)
        password.send_keys(args.Password)
        #sign in
        if args.Mode==1:
            time.sleep(1)
            signInButton.click()#game-details-play-button-container > button
            time.sleep(1)
            if (df[df.columns[0]].count()) >= -1 + C:
                os.rename(overflowfile, project_dir+"\\acounts"+'\\Squad_'+(df.columns[0])+".csv")

#captcha bypass/or bot will idealy go somewere here  ¯\_(ツ)_/¯ or sobhans nephew. idk
#==-=-==-===-====-===---------------=====-====-===-===-=====-=-=-=-=-=-=-=--==-----
        input()     

        print("starting friend request accept")
        #dangerous======================================================================================================================
        cookies = driver.get_cookies()
        for cookie in cookies:

            if cookie.get('name') == '.ROBLOSECURITY' :
                ROBLOSECURITY = cookie.get('value')
                print(cookie.get('value'))
        try:
            rpy.User.Internal.SetCookie(ROBLOSECURITY,True)
            rpy.User.Friends.Internal.SendFriendRequest(args.LeaderID)#not working. find out why
            print("RPY library ran.")
        except:
            print("first friend request failed")
            LeaderURL = "https://www.roblox.com/users/{}/profile".format(args.LeaderID)
            driver.get(LeaderURL)
            time.sleep(1)
            friendRequest = driver.find_element_by_class_name('btn-control-md')
            friendRequest.click()

        time.sleep(2)
        input()#check if user is ready to make the next bot
        
print(str(invalid)+" names failed.")
