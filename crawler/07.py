from urllib import request
import requests
from bs4 import BeautifulSoup
import urllib
import time

def directions():
	'''启动时的介绍'''
    print("\n===============欢迎使用 Yunmusic Download ================")
    print("**该软件可以下载网易云的音乐\n(包括付费下载曲目和免费曲目,但不包括已下架曲目和试听曲目)")
    print("使用方法:\n","在浏览器中打开歌单,复制歌单最后的一串数字\n","将该串数字粘贴到以下输入框中\n")
def get_content(url):
    response= requests.session()
    response= BeautifulSoup(response.get(url, headers=headers).content, "html.parser")
    return response

def save(response):
    '''以字典方式获取ID和歌名'''
    music_dict = {}
    result = response.find('ul', {'class': 'f-hide'}).find_all('a')
    for music in result:
        music_dict[music['href'].strip("/song?id=")] = music.text

    return music_dict

def down(ID,music_dict):
	'''下载音乐模块'''
    url='https://music.163.com/song/media/outer/url?id='
    req=requests.get(url+ID,headers=headers,allow_redirects=False)
    music_link=req.headers['Location']
    urllib.request.urlretrieve(music_link,music_dict[ID]+".mp3")

def down_load(music_dict):
    while True:
        ID=input("请输入音乐ID(输入q可以退出哦!):")
        if ID=="q":
            break
        elif ID=="ALL":
            for key,value in music_dict.items():
                try:
                    down(key,music_dict)
                    time.sleep(1.1)
                except FileNotFoundError:
                    print(music_dict[key],"下载失败!")
                    continue
            print("全部下载完毕!")
        else:
            try:
                down(ID,music_dict)
                print(music_dict[key],"下载完毕!")
            except KeyError:
                print("没有这个ID哦,请检查后再次尝试!")

if __name__=="__main__":
    directions()
    list_id=input("请输入歌单ID:")
    
    url="https://music.163.com/playlist?id="+list_id
    
    headers = {
    'Host': 'music.163.com',
    'Referer': 'https://music.163.com/',
    'User-Agent': '这里请输入自己的浏览器标识!!!'
    }
    
    response=get_content(url)
    for ID,name in save(response).items():
    	#打印音乐信息
        print("歌曲ID:",ID,"\t歌曲名字:",name)
    down_load(save(response))

