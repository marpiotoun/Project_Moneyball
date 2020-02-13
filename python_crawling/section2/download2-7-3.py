from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import urllib.parse as rep

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/tag-curation/tag/356"

res = req.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')
recommend = soup.select(".course_title")
# print(recommend)
for i, e in enumerate(recommend):
    print(i," : ", e.select_one(".title").string)