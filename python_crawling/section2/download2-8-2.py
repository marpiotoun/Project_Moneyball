from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req
import os
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.inflearn.com/tag-curation/tag/356"
# selector = "#main > section.section.section_1 > div.container.course_list > div > div:nth-child(7)"
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("#main > section.section.section_1 > div.container.course_list > div > div:nth-child(17) > div > a > div.card-image > figure > img")
print(img_list)

#main > section.section.section_1 > div.container.course_list > div > div:nth-child(7) > div > a > div.card-image > figure > img