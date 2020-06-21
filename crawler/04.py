
import requests

getHtmlHeaders={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
}
response = requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format("1432427879"), headers= getHtmlHeaders)
# response = requests.get("http://m801.music.126.net/20200326181648/7101aef1dcb930fbfe994218ab77c00c/jdymusic/obj/w5zDlMODwrDDiGjCn8Ky/1907460783/fa4f/3727/22b3/503a3bbaed02dbc34f52fc3a499ccdcc.mp3")
# music = response.headers['Location']
# response = requests.get(music)
# print(music)
print(response.url)
with open("crawler/music/01.mp3","wb") as f:
    f.write(response.content)
    f.flush()
