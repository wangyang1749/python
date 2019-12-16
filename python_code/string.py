a=[1,2,3,4,5,6]
b=a*5
print(b[::-1])
# 包括左边不包括右边
print(a[0:2])
print(len(a))
print(2 in a)
print(list(range(0,100,2)))
for i in range(1,10):
    print(i*i)

A="ATGC"
for i in A:
    print(i)

for i,j in enumerate(A):
    print(i,j)

a=[[1,2,3],[4,5,6],[7,8,9]]
print(a[2][1])

a={}
a["zs"]="male"
a["ls"]="female"
a["ww"]=[123,465,789]
print(a["zs"])
print(a["ww"])
print(a.keys())
for key in a.keys():
    print(a[key])

genome={}
genome["chr1"]="ATTG"*10
print(genome["chr1"][:5])

for i in range(10):
    if i%2==0:
        print(i)
    else:
        print(i*i)


for i in a.keys():
    if i=="zs":
        print(1)
    elif i=="ls":
        print(2)
    else:
        print(3)

a = 100
if a>=0:
    print(a)

print("{0} and {1}".format("aa","bb"))
# w以写的方式打开 a以追加的方式打开 
# r以读的模式打开 +以读写的模式打开 
# b以二进制的模式打开
f=open("Phyllothelys_breve-线粒体基因组拼接结果-纯序列版(FASTA格式).fasta","r")

for line in f:
    line = line.strip()
    print(line)
    break

f = open("02.txt","w")
with open("01.txt","r") as input_f:
    for line in  input_f:
        line =line.strip()
        result=int(line)* int(line)
        f.write(str(result)+"\n")
        print(result)
