n=int(input("enter the number: "))
num=1
# for i in range(n):
#     for j in range(n):
#         print(num,end=" ")
#         num=num+1
#     print(" ")

# for i in range(0,(n*n)+1):
#     print(i ,end="")
#     if i%n==0:
#         print("\n")

#reverse
for i in range((n*n),0,-1):
   
    if i%n==0:
        print("\n")
    print(i ,end="")
    