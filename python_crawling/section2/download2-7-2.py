from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/lastsearch2.nhn"
up = req.urlopen(url).read().decode('cp949')
soup = BeautifulSoup(up, "html.parser")
# print(soup)

# print(soup.prettify())

top20 = soup.select("div.box_type_l > table.type_5 > tr")
# for i, j in enumerate(top20, 1):
#     print("{} : {}".format(i, j.string))
#     if i == 20:
#         break
# for i, e in enumerate(top20):
#     print(i, " >>> " , e)
#
j=1
for i, e in enumerate(top20):
    if e.find("a") is not None:
        print(j, " : ", e.select_one(".tltle").string)
        j+=1

