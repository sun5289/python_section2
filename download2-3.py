import sys
import io

import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = 'http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg'
htmlUrl = 'http://google.com'
# urllib.request.urlretrieve(imgUrl,salvaPath)

salvaPath1 = 'D:/python/Crawling/section2/test/test.jpg'
salvaPath2 = 'D:/python/Crawling/section2/test/index.html'

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()


saveFile1 = open(salvaPath1,'wb') # w: write,r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(salvaPath2,'wb') as saveFile2:
    saveFile2.write(f2)


# dw.urlretrieve(imgUrl,salvaPath1)
# dw.urlretrieve(htmlUrl,salvaPath2)

print('다운로드 완료')
