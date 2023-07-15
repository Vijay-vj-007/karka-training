"""amounts=[100,200,300,400,500]
sum=0

for amount in amounts:
    sum=amount+sum
    print(sum)"""


#process runs inside for sum
"""
amounts=[100,200,300,400,500]
sum=0
enum_amounts=enumerate(amounts)
for i,amount in enum_amounts:
    print("entering iteration process for item no :"+str(i))
    print("before sum",sum)
    sum = amount+sum
    print("after sum" , sum)
    print("exiting iteration process for item no :" +str(i))
    print("\n")


"""








    