a=0
def f(x):
    global a;a = a+1;print(a)
    if x> 0 :
        return x + f(x-1)
    else:
        return 0
    
# print(f(5))

# 计算任意n个整数之和
def sum1(A,n):
    sum = 0 # O(1)
    for i in range(n): # O(n)
        sum+=A[i] # O(1)
    return sum # O(1)

# print(sum1([1,2,3,4],4))

# 减而治之 Decrease and conquer
def sum2(A,n):
    # global a;a = a+1;print(a)
    if n<1: 
        return 0 # 递归基
    else:
        res = sum2(A,n-1)+A[n-1]
    return res
print(sum2([1,2,3,4],4))
