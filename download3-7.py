import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req
from bs4 import BeautifulSoup as be


url = "http://finance.daum.net/"
res = req.urlopen(url).read()
soup = be(res,"html.parser")

# print('soup', soup.prettify())

top = soup.select("ul#topMyListNo1 > li")
# print(top)
for i,e in enumerate(top,1):
    # print('e :::',e)
    print(i,'e =>',e.find("a").string,e.find("span").string

    )
