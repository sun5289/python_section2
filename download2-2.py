import sys
import io

import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = 'http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg'
htmlUrl = 'http://google.com'
# urllib.request.urlretrieve(imgUrl,salvaPath)

salvaPath1 = 'D:/python/Crawling/section2/test.jpg'
salvaPath2 = 'D:/python/Crawling/section2/index.html'

dw.urlretrieve(imgUrl,salvaPath1)
dw.urlretrieve(htmlUrl,salvaPath2)

print('다운로드 완료')
