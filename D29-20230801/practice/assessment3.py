A=[1,5,7,3,8]
B=[2,4,3,7,2]
c=[]
for i in range(len(A)):
        if A[i]>B[i]:
                c=c+[A[i]]
        else:
            c=c+[B[i]]
print(c)



