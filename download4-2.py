import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req
from bs4 import BeautifulSoup as be


url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read()
soup = be(res,"html.parser")

# print('soup', soup.prettify())
top10 = soup.select("#siselist_tab_0 > tr")
# print(top10)
i = 1
for e in top10:
    if e.find("a") is not None:
        print(i," " ,e.select_one(".tltle").string)
        i  += 1
