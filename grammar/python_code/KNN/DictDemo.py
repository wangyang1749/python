import operator
a = {}
a['A']=a.get('A',0)+1
a['A']=a.get('A',0)+1
a['B']=a.get('B',0)+1
a['B']=a.get('B',0)+1
a['B']=a.get('B',0)+1
print(a)

b = sorted(a.items(),key=operator.itemgetter(1),reverse=True)
print(b)
for key in a.values():
    print(key)

student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
print(student_tuples)
print(sorted(student_tuples, key=lambda t: t[2]) )
print()
a3={'Asss':2,'B333':5}
def f1(c):
    print(c)
    return c[1]
# c = sorted(a3.items(),key=lambda c:c[1],reverse=True)
c = sorted(a3.items(),key=f1,reverse=True)
print(c)