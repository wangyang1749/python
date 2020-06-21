# -*-coding:utf-8-*-
import jieba
import re
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def getList(file_name):
  r = "[，。《》【】\s？、, ]+"
  word_list = []
  with open(file_name) as input_file:
      for line in input_file.readlines():
        line = line.strip()
        if not len(line):
          continue
        line = re.sub(r, "", line)
        words = jieba.lcut(line)
        word_list = word_list+words
  return word_list

def analyze(word_list):
  counts = {}
  for word in word_list:
    if len(word) == 2:
      counts[word] = counts.get(word, 0) + 1
      
  countsList = list(counts.items())
  countsList.sort(key=lambda x:x[1], reverse=True)
  list_word_result = []
  list_word_count = []
  for word,count in countsList:
    list_word_result.append(word)
    list_word_count.append(count)
  return list_word_result,list_word_count

def draw(list_word_result,list_word_count):
  plt.title('宋词三百首词频分析')
  color = ['b','r','g','y','c','m','y','k','c','g','g']
  plt.bar(list_word_result[:20],list_word_count[:20],width=0.5,color=color)
  plt.xticks(rotation = 90)
  plt.show()

if __name__ == "__main__":
    cotent = getList("词频分析/data.txt")
    list_word_result,list_word_count = analyze(cotent)
    draw(list_word_result,list_word_count)