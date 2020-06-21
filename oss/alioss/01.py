# -*- coding: utf-8 -*-
import oss2

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAI4FsLwhyviCa4BtTqUrvo', 'NIgxVFvknFxHjHdewnYrKV8Kv2uOMe')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'wangyang-bucket')






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
resp = requests.get("https://music.163.com/playlist?id=883623437",headers= getHtmlHeaders)

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
    input = requests.get('http://music.163.com/song/media/outer/url?id={}.mp3'.format(music_dict[music]), headers= getHtmlHeaders)
    
    
    result = bucket.put_object("music/"+music+".mp3", input)
    print('http status: {0}'.format(result.status))
    
    
    # print(response.url)
    # with open("crawler/music/{}.mp3".format(music),"wb") as f:
    #     f.write(response.content)
    #     f.flush()





# 上传文件
# 如果需要上传文件时设置文件存储类型与访问权限，请在put_object中设置相关headers, 参考如下。
# headers = dict()
# headers["x-oss-storage-class"] = "Standard"
# headers["x-oss-object-acl"] = oss2.OBJECT_ACL_PRIVATE
# result = bucket.put_object('<yourObjectName>', 'content of object', headers=headers)
# result = bucket.put_object('<yourObjectName>', 'content of object')

# with open('<yourLocalFile>', 'rb') as fileobj:
#     # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
#     fileobj.seek(1000, os.SEEK_SET)
#     # Tell方法用于返回当前位置。
#     current = fileobj.tell()
#     bucket.put_object('<yourObjectName>', fileobj)

# HTTP返回码。
# print('http status: {0}'.format(result.status))
# # 请求ID。请求ID是请求的唯一标识，强烈建议在程序日志中添加此参数。
# print('request_id: {0}'.format(result.request_id))
# # ETag是put_object方法返回值特有的属性。
# print('ETag: {0}'.format(result.etag))
# # HTTP响应头部。
# print('date: {0}'.format(result.headers['date']))