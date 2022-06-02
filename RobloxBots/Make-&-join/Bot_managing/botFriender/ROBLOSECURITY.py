
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def ROBLOSECURITY():
    current_dir = Path(__file__)
    project_dir = str([p for p in current_dir.parents if p.parts[-1]=='ROBO'][0])


    driver = webdriver.Chrome(str(project_dir)+r'\RobloxBots\Settings&Config\WebDriver\chromedriver.exe')
    driver.get("https://www.roblox.com/")

    cookies = driver.get_cookies()

    for cookie in cookies:


        if cookie.get('name') == '.ROBLOSECURITY' :
        
            print("=====================================================")
            print(cookie.get('value'))
            ROBLOSECURITY = cookie.get('value')

        return ROBLOSECURITY

            
                
                
              

