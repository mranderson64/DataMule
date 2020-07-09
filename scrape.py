import sys
import json
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from tbselenium.tbdriver import TorBrowserDriver
with TorBrowserDriver("/home/liam/DataMule/tor-browser/") as driver:
    driver.get('https://check.torproject.org')

with open('/home/liam/DataMule/urls.json') as json_file:
    data = json.load(json_file)

nameList = []
posList = []

sites = 2
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
    
nameListLen = len(nameList)    
    
while a < nameListLen:
    print(nameList[a])
    print(posList[a])
    if a == nameListLen:
        break
    i += 1
    
class versus:
    def __init__(self, pos, url, user, passw, memw):
        self.pos = pos
        self.url = url
        self.user = user
        self.passw = passw
        self.memw = memw