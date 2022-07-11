from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import argparse
import string
import random
import robloxpy as rpy
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
my_parser = argparse.ArgumentParser()

# Path to the .xlsx of bot passwords and usernames
my_parser.add_argument('ListPath',metavar='ListPath',type=str,help='the path to list')
# URL for leader account
my_parser.add_argument('LeaderURL',metavar='LeaderURL',type=str,help='the url for the leader account')
# The number of bot that will run
my_parser.add_argument('NumOfBots',metavar='NumOfBots',type=int,help='the num of bots to run')
# to use custom list of names or randomly generated one
my_parser.add_argument('Custom_random',metavar='Custom_random',type=str,help='Use custom(C) list or random(R) list')
#password that all the accounts will use
my_parser.add_argument('Password',metavar='Password',type=str,help='password that all the accounts will use')

# Execute the parse_args() method
args = my_parser.parse_args()

print(args.ListPath)
print(args.LeaderURL)
print(args.NumOfBots)
print(args.Custom_random)
print(args.Password)

#python Package\BotMaker\SemiAutoBotMaker.py https://www.roblox.com/users/177263364/profile 5 R "Password"

#root dir of project

#list of usernames to be used.
nameList = []

#==========================random name generator==========================
if args.Custom_random == "R":

    N = 18  #chars in username
    loops = 5  #number of usernames
    for i in range(loops):
        print("test")
        name = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))
        # name = input("name: ")
        # avalability
        if rpy.User.External.DoesNameExist(name) == "Unavailible":
            print("names are already taken")
        #underscore filtering
        elif (name[:1] == "_" or name[-1] == '_' or name.count('_') > 1):
            print("names are in valid")
        nameList.append(name)
        print(name)
        print(nameList)

#===========================gets username from custom list=====================
elif args.Custom_random =="C":
    
    with open(args.ListPath) as file:
        for line in file:
            print(line.rstrip())
            nameList.append(line.rstrip())
    print(nameList)
    

#sobhan1384

#===============================b-day vars=============================
bdaymonth='2'
bdayday='2'
bdayyear='2005'


print("test")


#enters username and password into roblox and goes to the game link.
count = 0
for x in zip(nameList):
    count = count + 1
    time.sleep(1)

    print(x)
    driver = webdriver.Chrome('C:\webdrivers\chromedriver') 
    driver.get("https://www.roblox.com/")
    time.sleep(2)
    usernameStr = x



    username = driver.find_element_by_id('signup-username')
    password = driver.find_element_by_id('signup-password')
    signInButton = driver.find_element_by_id('signup-button')
    # gender = driver.find_element_by_id(sex+"Button")
    month = driver.find_element_by_id("MonthDropdown")
    day = driver.find_element_by_id("DayDropdown")
    year = driver.find_element_by_id("YearDropdown")
    
    
    #BDAY:
    select = Select(month)
    select.select_by_value(bdaymonth)
    select = Select(day)
    select.select_by_value(bdayday)
    select = Select(year)
    select.select_by_value(bdayyear)
    username.send_keys(usernameStr)
    ValidationOutput = driver.find_element_by_id("signup-usernameInputValidation").text
    if ValidationOutput:
        print("Username cannot be used")
        print("Reason:", ValidationOutput)
    else:
        password.send_keys(args.Password)
        
        #sign in
        signInButton.click()#game-details-play-button-container > button
        time.sleep(2)

#user check captcha thing. basicaly just input()
#===============---------------====================-=-=-=-=-=-=-=--==
        input()
        # driver.get("https://www.roblox.com/users/177263364/profile")
        driver.get(args.LeaderURL)
        time.sleep(1)
        # friendRequest = driver.find_element_by_class_name('btn-control-md ng-binding ng-scope')
        friendRequest = driver.find_element_by_class_name('btn-control-md')
        friendRequest.click()
        time.sleep(2)
        input()#check if user is ready to make the next bot
        f = open('BotCounter.txt',"w")
        f.write(str(count))
        f.close()

    # print("do date of birth and press enter in cmd")
    # a = input("leave blank to continue or enter skip (s): ")
    # if a =="skip" or a == "s":
    #     print("skiped that one")
    # else:
        
    #     signInButton.click()#game-details-play-button-container > button
    #     time.sleep(2)
    #     input()# wait untill user has complated the captcha or
    #             #confirmed there is no captcha
    #     driver.get("https://www.roblox.com/users/177263364/profile")
    #     time.sleep(1)

    #     #add friend button
    #     friendRequest = driver.find_element_by_class_name('btn-control-md ng-binding ng-scope')
    #     friendRequest.click()
        
    #     time.sleep(2)
    #     c = input("press enter: ")
    #     f = open('BotCounter.txt',"w")
    #     f.write(str(count))
    #     f.close()
    #     if c =="dees nuts":
    #         print("fit dees nuts in yo mouth. HA HA, HA HA")

