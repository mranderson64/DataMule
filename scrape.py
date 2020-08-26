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
import versus
import tpds

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
    if nameList[a] == "tpds":
        pos = posList[a]
        url = data[pos]['URL']
        user = data[pos]['user']
        passw = data[pos]['password']
        memw = data[pos]['memword']
        print(url, user, passw, memw)
        tpdsScrape = tpds.tpds(url, user, passw, memw)
        tpdsScrape.scrape()
    elif nameList[a] == "versus":
        pos = posList[a]
        url = data[pos]['URL']
        user = data[pos]['user']
        passw = data[pos]['password']
        memw = data[pos]['memword']
        print(url, user, passw, memw)
        versusScrape = versus.versus(url, user, passw, memw)
        versusScrape.scrape()
    if i == sites-1:
        break
    i += 1
