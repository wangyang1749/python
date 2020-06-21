
# -*-coding:utf-8 -*-
'''
@File       : youdao.py
@Author     : HW Shen
@Date       : 2019/8/5
@Desc       :
'''
 
import urllib.parse
import http.client
import random
import hashlib
import xml.etree.ElementTree as et

# 通过在http://ai.youdao.com/ 执行以下操作获取
# 1.注册账号 => 2.创建应用 => 3.创建实例 => 4.应用绑定对象
appKey = '0eab2b213ecebbb4'
secretKey = 'kCLxx1EGYLGac4fKArclO8gEfnbtVcJX'
 
 
# 中译英
def Ch2En(item):
    httpClient = None
    myurl = '/api'
 
    fromLang = 'zh-CHS'  # 译文主体
    toLang = 'EN' # 译文客体
 
    salt = random.randint(1, 65536)
    sign = appKey + item + str(salt) + secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    
    # 拼接完整译文对象
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        item) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
 
    result = ""
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        print(response.read())
        result = eval(response.read().decode("utf-8"))['translation']
        # print(type(result))
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return result
 
 
# 英译中
def En2Ch(item):
    httpClient = None
    myurl = '/api'
 
    fromLang = 'EN' # 译文主体
    toLang = 'zh-CHS' # 译文客体
 
    salt = random.randint(1, 65536)
    sign = appKey + item + str(salt) + secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()

    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        item) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
 
    result = ""
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        resultJson = response.read().decode("utf-8")
        # print(resultJson)
        result = eval(resultJson)
        # print(result)
 
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return result
msg = """
<tr>
<td>{0}</td>
<td>
    <span class="phonetic">[{1}]</span>
    <i class="sound fsound" style="cursor:pointer" naudio="http://dict.youdao.com/dictvoice?type=2&audio={0}" title="美式发音">美</i>
</td>
<td>
    <span class="phonetic">[{2}]</span>
    <i class="sound fsound" style="cursor:pointer" naudio="http://dict.youdao.com/dictvoice?type=1&audio={0}" title="英式发音">英</i>
</td>
<td>{3}</td>
</tr>
"""
body  ="""
  <table>
    <thead>
      <tr>
        <th>单词</th>
        <th>美式发音</th>
        <th>英式发音</th>
        <th>翻译</th>
      </tr>
    </thead>
    <tbody>
     {0}
    </tbody>
  </table>
"""

# ["stem","tricky","workshop","weakness","violence","unpleasant","unfair","underground",
#                 "tremendous","trail","thrill","tasty","swell"]

# vocabularys = ["priority","aggressive","disruptive","treatment","jewelry","policy"]
# spouse,shelter,racial,pursuit,punishment,prosperous,prominent,politician,pilot,pale,pace,overwhelm,economist,economy,economic,technique,advantage
# zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twenty-one,twenty-two,twenty-three,twenty-four,twenty-five,twenty-six,twenty-seven,twenty-eight,twenty-nine,thirty,thirty-one,thirty-two,thirty-three,thirty-four,thirty-five,thirty-six,thirty-seven,thirty-eight,thirty-nine,forty,forty-one,forty-two,forty-three,forty-four,forty-five,forty-six,forty-seven,forty-eight,forty-nine,fifty,fifty-one,fifty-two,fifty-three,fifty-four,fifty-five,fifty-six,fifty-seven,fifty-eight,fifty-nine,sixty,sixty-one,sixty-two,sixty-three,sixty-four,sixty-five,sixty-six,sixty-seven,sixty-eight,sixty-nine,seventy,seventy-one,seventy-two,seventy-three,seventy-four,seventy-five,seventy-six,seventy-seven,seventy-eight,seventy-nine,eighty,eighty-one,eighty-two,eighty-three,eighty-four,eighty-five,eighty-six,eighty-seven,eighty-eight,eighty-nine,ninety,ninety-one,ninety-two,ninety-three,ninety-four,ninety-five,ninety-six,ninety-seven,ninety-eight,ninety-nine

vocabularys = """
zero
"""
vocabularys =  vocabularys.strip() # 去掉换行
vocabularys = vocabularys.split(",")

if __name__ == '__main__':
    result_table = ""
    for word in vocabularys:
        print("start:"+word)
        e2c = En2Ch(word)
        print(e2c)
        findWord = e2c['basic']

        uk_phonetic = '__'
        if "uk-phonetic" in findWord:
            uk_phonetic = e2c['basic']['uk-phonetic']
        us_phonetic = '__'
        if "us-phonetic" in findWord:
            us_phonetic = e2c['basic']['us-phonetic']

        explains = e2c['basic']['explains']
        explains = ','.join(explains)
        result_table+=msg.format(word,us_phonetic,uk_phonetic,explains)
    # print(result_table)
    print("success!")
    with open("youdao/output/01.html","w") as f:
        f.write(body.format(result_table).replace("\n",''))
    # print(msg.format("photosynthesis",explains,us_phonetic,uk_phonetic))

    # c2e = Ch2En('假日')
    # print("Ch2En:", c2e)
    # e2c = En2Ch("photosynthesis")
    # print(e2c['basic']['uk-phonetic'])
    # print(e2c['basic']['uk-speech'])
    # print(e2c['basic']['us-phonetic'])
    # print(e2c['basic']['us-speech'])
    # print(e2c['basic']['explains'])
   
    

