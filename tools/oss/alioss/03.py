# -*- coding: utf-8 -*-
import oss2
import requests
from sys import stdout
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAI4FsLwhyviCa4BtTqUrvo', 'NIgxVFvknFxHjHdewnYrKV8Kv2uOMe')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'wangyang-bucket')

def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()
# simplifiedmeta = bucket.get_object_meta("<yourObjectName>")

# print(bucket.head_object('video/01.mp4'))

getHtmlHeaders={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
}
input = requests.get('https://video-subtitle.tedcdn.com/talk/podcast/2018S/None/AlexanderBelcredi_2018S-480p-zh-cn.mp4', stream=True,headers= getHtmlHeaders)
flag = True
result= None

filesize = input.headers["Content-Length"]
print("文件大小:", filesize, "bytes")
chunk_size = 1024*1024
times = int(filesize) // chunk_size
show = 1 / times
show2 = 1 / times
start = 1
# bucket.put_object('video/02.mp4', input)
for chunk in input.iter_content(chunk_size=chunk_size):
    if flag:
        result = bucket.append_object("video/02.mp4",0, chunk)
        flag=False
        print("第一次上传")
    else:
        length = bucket.head_object('video/02.mp4').headers['Content-Length']
        print( result.next_position)
        print( length)
        bucket.append_object('video/02.mp4', length, chunk)
        print("不是第一次上传")





    # if start <= times:
    #         stdout.write(f"下载进度: {show:.2%}\r")
    #         start += 1
    #         show += show2
    #     else:
    #         stdout.write("下载进度: 100%")
    # print("\n结束下载")



# 设置首次上传的追加位置（Position参数）为0。
# 如果不是首次上传，可以通过bucket.head_object方法或上次追加返回值的next_position属性，得到追加位置。


# with open("alioss/video/01.mp4",'wb') as f:
#     filesize = input.headers["Content-Length"]
#     print("文件大小:", filesize, "bytes")

   
#     chunk_size = 1024*10
#     times = int(filesize) // chunk_size
#     show = 1 / times
#     show2 = 1 / times
#     start = 1
#     for chunk in input.iter_content(chunk_size=chunk_size):
#         f.write(chunk)
#         if start <= times:
#             stdout.write(f"下载进度: {show:.2%}\r")
#             start += 1
#             show += show2
#         else:
#             stdout.write("下载进度: 100%")
#     print("\n结束下载")
        # print("上传一次",1024*1024) # 一次一兆

# result = bucket.put_object("video/"+music+".mp4", input,progress_callback=percentage)
# print('http status: {0}'.format(result.status))
