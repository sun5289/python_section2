import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from bs4 import BeautifulSoup as be


with open("food-list.html",encoding="utf-8") as html:
        soup = be(html,'html.parser')

print("1 ==>" ,soup.select_one("li:nth-of-type(8)").string)
print("2 ==>" ,soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3 ==>" ,soup.select("#ac-list > li[data-lo='cn']")[0].string) # select 는 리스트로 반환 되기때문에 index로 구분 해줘야한다.
print("4 ==>" ,soup.select("#ac-list > li.alcohol.high")[0].sting)


param ={"data-lo" : "cn","class":"alcohol"}
print("5 ==>" ,soup.find("li",param).string)
print("6 ==>" ,soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    if ac["data-lo"] =="us":
        print("data-lo == us ",ac.string)
