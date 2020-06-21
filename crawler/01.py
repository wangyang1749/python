from urllib.request  import urlopen
import re
from bs4 import BeautifulSoup
html = urlopen("http://47.93.201.74/article/ec934275-1876-493f-b4f9-4e6f81997785.html").read().decode("utf-8")

# print(html)
# res = re.findall("<title>(.*?)</title>",html,flags=re.DOTALL)
# print(res[0])

soup = BeautifulSoup(html,features='lxml')
# print(soup.h1)

all_href = soup.find_all('a')
all_href = [l for l in all_href]
# print(all_href)

text = soup.find_all("li",{'class':'breadcrumb-item'})
text = [l.get_text() for  l in text]
print(text)