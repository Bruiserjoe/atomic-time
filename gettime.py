import requests
import time
from bs4 import BeautifulSoup
while(1):
    r = requests.get('https://www.timeanddate.com/worldclock/fullscreen.html?n=4757')
    src = r.content
    soup = BeautifulSoup(src, 'html.parser')
    out = soup.find(id="i_time")
    print(out.string)
    time.sleep(1)

