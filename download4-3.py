import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request as req
from bs4 import BeautifulSoup as be
import urllib.parse as rep


base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌") # 한글은 유니코드로 인코딩 해준다.

url = base + quote
res = req.urlopen(url).read()
soup = be(res,"html.parser")

recommand = soup.find_all("span.rank_cont > li")
print(recommand)

# for i ,e in enumerate(recommand,1):
#     print(i , e.select_one("h4.block_title > a").string)

for e in recommand:
    if e.find("a") is not None:
        print(i," " ,e.select_one(".tltle").string)
        i  += 1
