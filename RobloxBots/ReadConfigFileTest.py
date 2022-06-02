
from configparser import ConfigParser


print("hello world")

# options = webdriver.ChromeOptions()   
# driver = webdriver.Chrome("C:\ChromeDriver", options=options)

#Read config.ini file
config_object = ConfigParser()
config_object.read("RobloxBots\Settings&Config\config.ini")

#Get the password
path = config_object["PATHS"]

print(path["ChromeDriver"])
