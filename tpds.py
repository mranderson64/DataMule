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
with open('/home/liam/DataMule/config.json') as json_file:
    config = json.load(json_file)

mydb = mysql.connector.connect(
  host=config[0]['host'],
  user=config[0]['user'],
  password=config[0]['pass'],
  database=config[0]['name']
)
sequel = mydb.cursor()

class tpds:
    def __init__(self, url, user, passw, memw):
        self.url = url
        self.user = user
        self.passw = passw
        self.memw = memw

    def scrape(self):



        with TorBrowserDriver("/home/liam/DataMule/tor-browser/") as driver:
            i = 1

            while i < 7:
                driver.get(self.url+'?cat='+str(i)+'00')
                js = 'var listingData=\"[\";drugTitle=function(a){q=\"tbody:nth-child(2) > tr:nth-child(\"+a+\") > td:nth-child(1)\";return document.getElementsByClassName(\"table1\")[0].querySelector(q).innerText};drugCat=function(a){return document.querySelector(\"html body div#main h3\").innerText};drugLocation=\"\";drugStock=function(a){if(document.getElementsByClassName(\"table1\")[0].querySelector(\"tbody:nth-child(2) > tr:nth-child(\"+a+\") > td:nth-child(3)\").innerText==\"Sold out\"){return\"Sold out\"}else{return\"in stock\"}};drugSales=\"\";drugPrice=function(a){return parseFloat(document.getElementsByClassName(\"table1\")[0].querySelector(\"tbody:nth-child(2) > tr:nth-child(\"+a+\") > td:nth-child(2)\").innerText.split(\"=\")[0])};drugCurrency=\"USD\";drugUnit=\"\";var tableLen;for(i=1;i<99;i++){test=document.getElementsByClassName(\"table1\")[0].querySelector(\"tbody:nth-child(2) > tr:nth-child(\"+i+\")\");if(test==null){tableLen=i;break}}for(i=1;i<tableLen;i++){if(i==tableLen-1){last=\"]\"}else{last=\",\"}listingData=listingData+\'{\"title\":\"\'+drugTitle(i)+\'\",\"cat\":\"\'+drugCat(i)+\'\",\"loc\":\"\'+drugLocation+\'\",\"stock\":\"\'+drugStock(i)+\'\",\"sales\":\"\'+drugSales+\'\",\"price\":\"\'+drugPrice(i)+\'\",\"currency\":\"\'+drugCurrency+\'\",\"unit\":\"\'+drugUnit+\'\"}\'+last};return listingData'
                jsonD = driver.execute_script(js)
                pageData = json.loads(jsonD)
                print(pageData)
                sql = "INSERT INTO `Drugs`(`Advert title`, `Category`, `Location`, `Stock`, `Sales`, `Price`, `Units`, `Currency`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])"
                a = 0
                while a < len(pageData):
                    val = (pageData[a]['title'], pageData[a]['cat'], pageData[a]['loc'], pageData[a]['stock'], pageData[a]['sales'], pageData[a]['price'], pageData[a]['currency'], pageData[a]['unit'])
                    sequel.execute(sql, val)
                    mydb.commit()
                if i == 6:
                    break
                i += 1
        mydb.close()
