import re
rule1 = re.compile('^[a-zA-Z]{2}.*$')

rule2 = re.compile('^.*[a-zA-Z]{1}$')

excludes = ['the', 'of', 'to', 'and', 'in', 'a', 'is', 'were', 'was', 'you',
            'I', 'he', 'his', 'there', 'those', 'she', 'her', 'their',
            'that', '[a]', '[b]', '[c]', '[d]', 'them', 'or','for','as',
            'are','on','it','be','with','by','have','from','not','they',
            'more','but','an','at','we','has','can','this','your','which','will',
            'one','should','points)','________','________.','all','than','what',
            'people','if','been','its','new','our','would','part','may','some','i',
            'who','answer','when','most','so','section','no','into','do','only',
            'each','other','following','had','such','much','out','--','up','these',
            'even','how','directions:','use','because','(10','time','(15','[d].',
            '-','it.','[b],','[a],','however,','1','c','1.','2.','b','d','a','(10',
            '2','12.','13.','29.','3.','4.','5.','6.','7.','8.','9.','10.','11.','14.',
            '15.','【答案】a','【答案】d','【答案】b','【答案】c','c)','b)','a)','d)',
            'a),','b),','d).','c),']
#自行过滤简单词，太多了不写了
def getTxt():
    txt = open('vocabulary/EnglishText.txt').read()
    txt = txt.lower()
    # for ch in '!"@#$%^&*()+,-./:;<=>?@[]_`~{|}': #替换特殊字符
    #     txt.replace(ch, ' ')
    return txt

#1.获取单词
EngTxt = getTxt()

#2.切割为列表格式
txtArr = EngTxt.split()

#3.遍历统计
counts = {}
for word in txtArr:
    if word  not in excludes and rule1.match(word) is not None :
        # print(rule2.match(word) is  None,word)
        if rule2.match(word) is  None:
            word = word[:-1]
        # print(rule2.match(word) is  None,word)
        counts[word] = counts.get(word, 0) + 1
print(counts)        
#4.转换格式，方便打印，将字典转换为列表
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True)#排序
print(countsList)
print(len(countsList))
#5.打印
for word,count in countsList:
    with open('vocabulary/output_1.txt','a+') as f:
        str1=word+' : '+str(count)+ '次'
        f.writelines('<li>{0:15} - {1:10} </li>\n'.format(word,count))
        f.close()
    print('<li>{0:15} - {1:10} </li>'.format(word,count))