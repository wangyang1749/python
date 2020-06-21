import os
import  jieba

needWord = {"种族歧视":1,"种族":1}

# 判断词语是否在情感得分中
def isNeedWord(word):
    return word in needWord

# 排序
def sortWord(counts):
    items = list(counts.items())   #将键值对转换成列表
    items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序
    return items

# 打印列表
def showList(items,n):
    for i in range(n):
        word, count = items[i]
        print("{0:<5}{1:>5}".format(word, count))

# 词频分析
def wordCounts(words):
    counts = {}     # 通过键值对的形式存储词语及其出现的次数
    for word in words:
        if word in needWord:
            counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
    return calculate(counts)

# 以年分组统计
def calculate(counts):
    countsByYear = sum([value for value in counts.values()])
    # 得分的计算方式
    scoreByYear = sum([(needWord[key] *value) for key,value in counts.items()])
    return (countsByYear,scoreByYear)

# 打印map
def showMap(map):
    for key,value in map.items():
        countsByYear,scoreByYear=value
        print("{0:<20} 词频:{1:<5} 得分：{2}".format(key, countsByYear,scoreByYear))





def analyzeText(input_path):
    wordMap = {}
    for file_name in os.listdir(input_path):
        with open("{0}/{1}".format(input_path,file_name),"r") as input_file:
            content = input_file.read()
            # 分词
            words = jieba.lcut(content)
            # 以年分组统计
            wordMap[file_name] = wordCounts(words)
    showMap(wordMap)
    # print(wordMap)

if __name__ == "__main__":
    analyzeText("/home/wy/Documents/python/project02/resource")

    