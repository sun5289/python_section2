import sys
import io

import pytube
import os
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

down_dir = "D:/python/Crawling/section2/test"
yt = pytube.YouTube("https://www.youtube.com/watch?v=CTRO5NXmAp8") #다운받을 동영상 URL 지정
videos = yt.streams.all()

# print(len(videos))
#
# for i in range(len(videos)):
#     print(i ,' , ',videos[i])

cNum = int(input("다운 받은 화질은?? [0~21 입력]"))
videos[cNum].download(down_dir)
newFileName = input("변환 할 mp3 파일명은??")


oldFileName = videos[cNum].default_filename

subprocess.call(["ffmpeg","-i",
               os.path.join(down_dir,oldFileName),
               os.path.join(down_dir,newFileName)

               ])

print("완료!!")
