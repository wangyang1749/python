# 导入SnowNLP库
from snownlp import SnowNLP

# 需要操作的句子
text = '你站在桥上看风景，看风景的人在楼上看你。明月装饰了你的窗子，你装饰了别人的梦'

s = SnowNLP(text)

# 分词
print(s.words)

print(s.sentiments)
print(s.summary())


text1 = '这部电影真心棒，全程无尿点'
text2 = '这部电影简直烂到爆'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
print(text1, s1.sentiments) # 这部电影真心棒，全程无尿点 0.9842572323704297
print(text2, s2.sentiments) # 这部电影简直烂到爆 0.0566960891729531