# -*- coding: utf-8 -*-
import oss2
import sys
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAI4FsLwhyviCa4BtTqUrvo', 'NIgxVFvknFxHjHdewnYrKV8Kv2uOMe')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-beijing-internal.aliyuncs.com', 'wangyang-bucket')
def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()

input=sys.argv[1]
with open(input, 'rb') as fileobj:
    bucket.put_object('video/'+input.split('/')[-1], fileobj,progress_callback=percentage)
    