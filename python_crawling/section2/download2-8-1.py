from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("연예")
url = base + quote
print(url)

res = req.urlopen(url)
savePath = "/Users/sangsoohan/Documents/Programing_Project/Project_Moneyball/python_crawling/section2/img_download2-8-1/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
        print("add path")
except OSError as e:
    if e.errno != e.errno.EEXIST: #파일을 새로 만드는데 이미 파일이 존재할 경우 발생하는 에러코드
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
selector = "#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div.img_area > a.thumb._thumb > img"
img_list = soup.select(selector)
for i, img in enumerate(img_list, 1):
    # print(img['data-source'])
    fullFileName = os.path.join(savePath, "Lion"+str(i)+'.jpg')
    # print(fullFileName)
    req.urlretrieve(img['data-source'], fullFileName)

print("다운로드 완료")