# a=5
# for i in range(a):
#     for j in range(i+1):
#         print("* ",end="")
#     print("")    

# for i in range(a,0,-1):
#     for j in range(i-1):
#         print("* ",end="")
#     print("")


n=int(input("enter the number: "))
for i in range(1,n*2):
    if i<=n:
        a=i
    else:
        a=(n*2)-i
    for j in range(a):
        print("* ",end="")
    print("")
