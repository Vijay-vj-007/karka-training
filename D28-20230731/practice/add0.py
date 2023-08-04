a=[1,0,2,3,0,4,5,0]
B=[]
c=[]
for i in a:
    B+=[i]
    if i == 0:
        B+=[0]
for j in range(0,len(a)):
    c+=[B[j]]
print(c)
