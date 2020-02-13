import sys
import io
# from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net1">daum</a></li>
    <li><a href="http://www.daum.net2">daum</a></li>
    <li><a href="http://www.daum.net3">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a", string=["daum", "google"])
print(links)

#
# for a in links:
#     print('a, type(a), a')
#     href = a.attrs['href']
#     txt = a.string
#     # print(txt, ">", href)