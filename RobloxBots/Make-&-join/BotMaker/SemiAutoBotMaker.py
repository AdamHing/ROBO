import datetime
from sys import int_info
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import string,random,argparse
import robloxpy as rpy
import os,csv,time
import pandas as pd
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
from random import randint

#redus beacon/ pipeline/ talk to other programs fast. 
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
# test mode or run mode
my_parser.add_argument('Mode',metavar='Mode',type=int,help='testing mode(0) or working mode(1)')
# the number of bots that will be in each squad recomended 16
my_parser.add_argument('Squad_size',metavar='Squad_size',type=int,help='the number of bots that will be in each squad')
# Execute the parse_args() method
args = my_parser.parse_args()

print(args.LeaderID)
print(args.NumOfBots)
print(args.Password)
print(args.Mode)
print(args.Squad_size)

#==========================random valid name generator==========================("valid" = filterout bad substrings)
blacklist = []
#takes words out of csv and puts them into a single list.
with open(dir_path+ r"\bad-words3.csv", newline='') as inputfile:
    for row in csv.reader(inputfile):
        blacklist.append(row[0])

C = args.Squad_size 

N = 18              # name length

overflowfile =project_dir +"\\acounts"+"\\overflow"+".csv"# path var

invalid = 0
for i in range(args.NumOfBots):
    #================================= gererate random name=====================================
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
#===========================generate birthday=============================================
 #generate birth day
    #seed(1)
    bdayday = str(randint(1, 30))
    bdayyear = str(randint(2000, 2010))
    month_num = str(randint(1, 12))
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    bdaymonth = datetime_object.strftime("%B")
    if (len(bdayday) < 2):
        bdayday ="0"+ bdayday
#===========================make the bot=========================================
#enters username and password into roblox and goes to the game link.
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
    select = Select(month)
    select.select_by_visible_text(bdaymonth)

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
            print("test")
            print(args.Password)
            password.send_keys(args.Password)
        #sign in
    
        time.sleep(1)
        signInButton.click()#game-details-play-button-container > button
        time.sleep(1)
        if (df[df.columns[0]].count()) >= -1 + C:
            os.rename(overflowfile, project_dir+"\\acounts"+'\\Squad_'+(df.columns[0])+".csv")
#captcha bypass/or bot will idealy go somewere here  ¯\_(ツ)_/¯ or sobhans nephew. idk
#==-=-==-===-====-===---------------=====-====-===-===-=====-=-=-=-=-=-=-=--==-----
    input("finished/no captcha. press enter here: ")     

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
    input("Ready for next bot. press enter here: ")#check if user is ready to make the next bot
    # driver.quit()
        
print(str(invalid)+" names failed.")
