
import os
import requests
 
"""
下载M3U8文件里的所有片段
"""
 
def download(url):
    download_path = "crawler/video"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text # 获取M3U8的文件内容

    file_line = all_content.split("\n") # 读取文件里的每一行

    # # 通过判断文件头来确定是否是M3U8文件
    # if file_line[5]
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
      
        unknow = True   # 用来判断是否找到了下载的地址
        for index, line in enumerate(file_line):
            if "EXTINF" in line:
                unknow = False
                    # 拼出ts片段的URL
                pd_url = url.rsplit("/", 1)[0] + "/" + file_line[index + 1]
                # print(file_line)
                res = requests.get(pd_url)
                print(res.url)
                # c_fule_name = str(file_line[index + 1])
               
                with open(download_path + "/01.ts", 'ab') as f:
                    f.write(res.content)
                    print("download")
                    f.flush()
        if unknow:
            raise BaseException("未找到对应的下载链接")
        else:
            print("下载完成")
 
if __name__ == '__main__':
    download("https://hls.ted.com/videos/EmmaBryce_EndocrineSystem_2018E/video/600k.m3u8?nobumpers=true&qr=true&uniqueId=6a48f910")
