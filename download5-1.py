import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
import os
import urllib.request as req
from bs4 import BeautifulSoup as be
import urllib.parse as rep


base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("아이유")
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

img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i,img in enumerate(img_list,1):
    # print(img["data-source"])
    fullFileName = os.path.join(savePath,savePath+str(i)+'.jpg')
    # print(fullFileName)
    req.urlretrieve(img['data-source'],fullFileName)

print("download OK!!")
