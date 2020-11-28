import jieba
import re
 
class Scan(object):
    def __init__(self,path):
        self.path = path
    def scan(self):
        r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        try:
            f = open(self.path, "r",encoding='UTF-8')
        except Exception as err:
            print(err)
        finally:
            print("文件读取结束")
        word_list = []
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                line = re.sub(r, '', line)
                seg_list = jieba.cut(line, cut_all=False)
                word_list.append(list(seg_list))
            else:
                break
        f.close()
        print(word_list)
 
 
 
 
'''
分词并提取关键词
'''
import sys
sys.path.append('../')
 
import jieba
import jieba.analyse
from optparse import OptionParser
 
USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"
 
parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()
 
 
if len(args) < 1:
    print(USAGE)
    sys.exit(1)
 
file_name = "data.txt"
 
if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)
 
if opt.withWeight is None:
    withWeight = False
else:
    if int(opt.withWeight) is 1:
        withWeight = True
    else:
        withWeight = False
 
content = open(file_name, 'rb').read()
 
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)
 
if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
else:
    print(",".join(tags))