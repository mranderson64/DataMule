import sys
import json
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from tbselenium.tbdriver import TorBrowserDriver
with TorBrowserDriver("\liam\home\DataMule\tor-browser\\") as driver:
    driver.get('https://check.torproject.org')

with open('urls.json') as json_file:
    data = json.load(json_file)

dataLen = len(data[0][0])
i = 0

while i < dataLen:
    print i + ": " + data[0][i]
    i += 1

#class versus:   