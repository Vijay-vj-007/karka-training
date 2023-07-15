amounts=[100,200,300,400,500]
sum=0

for amount in amounts:
    sum=amount+sum
    print("sum",sum)
    average=sum/len(amounts)
    print("average",average)

