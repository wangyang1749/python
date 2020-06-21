import requests
getHtmlHeaders={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
}
response = requests.get(url='https://www.bilibili.com/video/av26522634', headers= getHtmlHeaders)
print(response.status_code)
if response.status_code == 200:
    print(response.text)
