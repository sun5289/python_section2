import sys
import io

import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = 'https://ssl.pstatic.net/tveta/libs/1181/1181173/30ca21eee566cb8d90c7_20180316172803976.jpg'
mp4Url = 'https://tvetamovie.pstatic.net/libs/1187/1187009/69b3c6581da2ab66f4b3_20180226153111982.mp4-pBASE-v0-f49384-20180226153402116.mp4'
# urllib.request.urlretrieve(imgUrl,salvaPath)

salvaPath1 = 'D:/python/Crawling/section2/test/homework.jpg'
salvaPath2 = 'D:/python/Crawling/section2/test/homework.mp4'

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(mp4Url).read()

with open(salvaPath1,'wb') as filejpg:
    filejpg.write(f1)

with open(salvaPath2,'wb') as filemp4:
    filemp4.write(f2)



print('다운로드 완료')
