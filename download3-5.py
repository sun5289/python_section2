import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from bs4 import BeautifulSoup as be
import re #regex

html ="""
    <html><body>
    <ul>
        <li><a id = "naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistoryr</a></li>
    </ul>
    </body></html>

"""

soup = be(html,'html.parser')
print(soup.find(id="naver").string)


li = soup.find_all(href=re.compile(r"da"))
for e in li:
    print(e.attrs["href"])
