import requests
from bs4 import BeautifulSoup
response= requests.session()
headers = {
'Host': 'music.163.com',
'Referer': 'https://music.163.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
response= BeautifulSoup(response.get("https://music.163.com/playlist?id=4858297474", headers=headers).content, "html.parser")
print(response)
music_dict = {}
result = response.find('ul', {'class': 'f-hide'}).find_all('a')
# print(result)

