from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net"
up = req.urlopen(url).read()
soup = BeautifulSoup(up, 'html.parser')

selector = "#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li:nth-child({}) > div > div:nth-child(1) > span.txt_issue > a"


def Print_Issue_And_Link(selector, num):
    #검색어를 출력
    print(num, "위: ", soup.select_one(selector.format(num)).string)
    print("link: ", soup.select_one(selector.format(num)).attrs['href'])

for i in range(1,21):
    if soup.select_one(selector.format(i)):
        Print_Issue_And_Link(selector, i)
    else:
        pass

