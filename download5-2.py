import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import os
import urllib.request as req
from bs4 import BeautifulSoup as be
import urllib.parse as rep


base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote

res = req.urlopen(url).read()
savePath = "D:/python/Crawling/section2/downimg/"

# 이미지 폴더 확인 및 생성 하기
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError:
    if e.errno != errno.EExist:
        print("폴더 만들기 실패!!")
        raise


soup = be(res,"html.parser")

img_list = soup.select("ul.slides")[1]

print(img_list)

for i,e in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)

    fullFileName = os.path.join(savePath,savePath+str(i)+'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullFileName)

print("download OK!!")
