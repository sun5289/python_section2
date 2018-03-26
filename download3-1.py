import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(">>",urljoin(baseUrl,"b.html"))
print(">>",urljoin(baseUrl,"sub/b.html"))
print(">>",urljoin(baseUrl,"../index.htm"))

print(">>",urljoin(baseUrl,"../img/img.jpg"))
print(">>",urljoin(baseUrl,"../css/css.jpg"))
