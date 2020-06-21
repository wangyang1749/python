'''
anki选择题的制作：
输入格式：
1、遗传的基本原理是由（孟德尔）揭示的
'''
import re
result=""
with open("anki/cloze.txt") as input_file:
    for line in input_file:
        line = line.strip()
        line = re.sub(r'{', "({{c1::",line )
        line = re.sub(r'}', "}}）", line)
        result+=line+"\n"
       
print(result)
with open("anki/result.txt","w") as output_file:
    output_file.write(result)




 

 

