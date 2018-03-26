import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req
from bs4 import BeautifulSoup as be
import urllib.parse as rep
import re #regex

# tit_hotissue


url = "https://www.daum.net/"
# quote = rep.quote_plus("추천-강좌") # 한글은 유니코드로 인코딩 해준다.
#
# url = base + quote

res = req.urlopen(url).read()
soup = be(res,"html.parser")


realcommant = soup.select("ol.list_hotissue.issue_row > li")
#
# print('111 =>' ,realcommant)

# li = soup.find_all(href=re.compile(r"https://search.daum.net/search"))

for i,e in enumerate(realcommant,1):

    print(i , e.select_one("a").string)
#
# recommand = soup.select("ul.slides")[0]
# print(recommand)
#
# for i ,e in enumerate(recommand,1):
#     print(i , e.select_one("h4.block_title > a").string)



# url = "https://www.inflearn.com/%EC%B6%94%EC%B2%9C-%EA%B0%95%EC%A2%8C/"
# res = req.urlopen(url).read()
# soup = be(res,"html.parser")
#
# # print('soup', soup.prettify())
# top10 = soup.select("#siselist_tab_0 > tr")
# # print(top10)
# i = 1
# for e in top10:
#     if e.find("a") is not None:
#         print(i," " ,e.select_one(".tltle").string)
#         i  += 1
