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

dataLen = len(data[0])
i = 0

while i < dataLen:
    line = data[i]['name']
    print str(i) + ": " + str(line)
    if i == dataLen:
        break
    i += 1

#class versus:   