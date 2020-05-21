import sys
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from tbselenium.tbdriver import TorBrowserDriver
with TorBrowserDriver("/liam/home/DataMule/tor-browser/") as driver:
    driver.get('https://check.torproject.org')

