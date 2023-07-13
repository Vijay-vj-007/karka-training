item1=int(input("enter the amount of item 1 : "))
item2=int(input("enter the amount of item 2 : "))
item3=int(input("enter the amount of item 3 : "))
item4=int(input("enter the amount of item 4 : "))
total_amount=(item1+item2+item3+item4)
if  total_amount >= 500 and total_amount <= 1000:
    Token="silver"
if total_amount > 1000:
    Token="Golden"
if total_amount < 500:
    Token="no"
print("you have won ",Token,"token")

