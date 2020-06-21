'''
下载网易云的每个区
'''
import requests
import re
from urllib.request  import urlopen


getHtmlHeaders={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
}
# html = urlopen("http://47.93.201.74/admin").read().decode("utf-8")

# resp = requests.get("https://music.163.com/discover/toplist?id=3198681354",headers= getHtmlHeaders)
resp = requests.get("https://music.163.com/playlist?id=4950971612",headers= getHtmlHeaders)

from bs4 import BeautifulSoup
soup = BeautifulSoup(resp.text,features='lxml')
all_href = soup.find_all('a',{'href':re.compile('/song\?id=(\d+)')})
# all_href = [l for l in all_href]
# print(all_href)
pattern = re.compile('/song\?id=(\d+)')
music_dict = {}
for music in all_href:
    # print(pattern.findall(l['href']))
    music_dict[music.text] = pattern.findall(music['href'])[0]
    # print(music.text,pattern.findall(music['href'])[0])
for music in music_dict:
    print("正在下载音乐:"+music)
    response = requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(music_dict[music]), headers= getHtmlHeaders)

    print(response.url)
    with open("crawler/music/{}.mp3".format(music),"wb") as f:
        f.write(response.content)
        f.flush()