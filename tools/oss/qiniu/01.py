# from qiniu import Auth
# q = Auth("5fGlYpm9h2xN86wWnV5XFvj2ifo3cK4SqNIqszCP", "gldkQYBiD062B-0AlNoqS-k85fURNE6RYU94v21N")


from qiniu import Auth, put_file, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = '5fGlYpm9h2xN86wWnV5XFvj2ifo3cK4SqNIqszCP'
secret_key = 'gldkQYBiD062B-0AlNoqS-k85fURNE6RYU94v21N'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'wangyang1749'
#上传后保存的文件名
key = 'my-python-logo.mp3'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
localfile = 'crawler/music/ 一抹桃花.mp3'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)