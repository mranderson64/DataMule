import sys
import json
import time
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
  password=config[0]['pass'],
  database=config[0]['name']
)
sequel = mydb.cursor()
    
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
            newURL = driver.current_url + '&ipp=100'
            driver.execute_script("window.location.href = '"+newURL+"';") #WHY DOES THE TOR MODULE NOT HAVE NAVIGATION 
            sleep(100)
            pages = driver.find_element(By.XPATH, '/html/body/section[3]/div/div[2]/div[304]/div[2]').get_text(strip=True)
            print(pages)
            
            totalPages = 99
            
            i = 0
            
            while i < totalPages:
                js = 'var listingData=\"[\";drugTitle=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)\").innerText};drugCat=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)\").innerText};drugLocation=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)\").innerText};drugStock=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)\").innerText};drugSales=function(c){return document.getElementsByClassName(\"listings__product\")[c].querySelector(\"table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)\").innerText};drugPrice=function(c){return parseFloat(document.getElementsByClassName(\"listings__price\")[c].querySelector(\"table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > strong:nth-child(1) > span:nth-child(1)\").innerText)};drugCurrency=function(c){a=document.getElementsByClassName(\"listings__price\")[c].querySelector(\"table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > strong:nth-child(1) > span:nth-child(1)\").innerText;b=a.split(\" \");return b[1]};drugUnit=function(c){return document.getElementsByClassName(\"listings__price\")[c].querySelector(\"table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1)\").innerText};listing=document.getElementsByClassName(\"listings__product\");for(i=0;i<listing.length;i++){if(i==listing.length-1){last=\"]\"}else{last=\",\"}listingData=listingData+\'{\"title\":\"\'+drugTitle(i)+\'\",\"cat\":\"\'+drugCat(i)+\'\",\"loc\":\"\'+drugLocation(i)+\'\",\"stock\":\"\'+drugStock(i)+\'\",\"sales\":\"\'+drugSales(i)+\'\",\"price\":\"\'+drugPrice(i)+\'\",\"currency\":\"\'+drugCurrency(i)+\'\",\"unit\":\"\'+drugUnit(i)+\'\"}\'+last};return listingData'
                json = driver.execute_script(js)
                pageData = json.load(json)
                print(pageData)
                #sql = "INSERT INTO `Drugs`(`Advert title`, `Category`, `Location`, `Stock`, `Sales`, `Price`, `Units`, `Currency`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])"
                #sequel.execute(sql, val)
                #mydb.commit()
                if i == totalPages-1:
                    break
                i += 1
        mydb.close()

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
    