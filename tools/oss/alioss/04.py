# -*- coding: utf-8 -*-
import oss2
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAI4FsLwhyviCa4BtTqUrvo', 'NIgxVFvknFxHjHdewnYrKV8Kv2uOMe')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', 'wangyang-bucket')
print(bucket.head_object('video/01.mp4').headers['Content-Length'])

# # 设置首次上传的追加位置（Position参数）为0。
# result = bucket.append_object('text/01.txt', 0, 'content of first append')
# # 如果不是首次上传，可以通过bucket.head_object方法或上次追加返回值的next_position属性，得到追加位置。
# bucket.append_object('text/01.txt', result.next_position, 'content of second append')
	