
def bubbleSort(A,n):
    stored=False
    while not stored:
        
        print(n)
        stored=True
        for i in range(1,n):
            if A[i-1]>A[i]:
                temp = A[i-1]
                A[i-1]=A[i]
                A[i]=temp
                stored=False
        n=n-1
if __name__ == "__main__":
    A=[9,8,5,2,6,7]
    bubbleSort(A,len(A))
    print(A)
