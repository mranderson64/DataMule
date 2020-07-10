import sys
import json
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from tbselenium.tbdriver import TorBrowserDriver

with open('/home/liam/DataMule/urls.json') as json_file:
    data = json.load(json_file)
    
with open('/home/liam/DataMule/config.json') as json_file:
    config = json.load(json_file)    

mydb = mysql.connector.connect(
  host=config[0]['host'],
  user=config[0]['user'],
  password=config[0]['pass']
)    
    
class versus:
    def __init__(self, url, user, passw, memw):
        self.url = url
        self.user = user
        self.passw = passw
        self.memw = memw
        
    def scrape(self):
    
        with TorBrowserDriver("/home/liam/DataMule/tor-browser/") as driver:
            driver.get(self.url)
            driver.find_element(By.XPATH, '/html/body/section[3]/div/div/form/input[1]').send_keys(self.user)
            driver.find_element(By.XPATH, '/html/body/section[3]/div/div/form/input[2]').send_keys(self.passw)
            driver.find_element(By.XPATH, '/html/body/section[3]/div/div/form/input[5]').click()
            driver.get(driver.url + '&ipp=100')
            pages = driver.find_element(By.XPATH, '/html/body/section[3]/div/div[2]/div[304]/div[2]').get_text(strip=True)
            print(pages)
            #mycursor.execute(sql, val)
        

nameList = []
posList = []

sites = config[0]['sites']
i = 0
a = 0

while i < sites:
    try:
        line = data[i]['name']
    except:
        print("ya goofed liam")
    print(str(i) + ": " + str(line))
    nameList.append(line)
    posList.append(i)    
    
    if i == sites-1:
        break
    i += 1
    
    
while a < sites:
    if nameList[a] == "versus":
        pos = posList[a]
        url = data[pos]['URL']
        user = data[pos]['user']
        passw = data[pos]['password']
        memw = data[pos]['memword']
        print(url, user, passw, memw)
        versusScrape = versus(url, user, passw, memw)
        versusScrape.scrape()
    if i == sites-1:
        break
    i += 1
    