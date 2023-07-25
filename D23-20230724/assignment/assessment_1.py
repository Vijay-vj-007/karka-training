number_1=int(input("Enter the number 1: "))
number_2=int(input("Enter the number 2: "))
number_3=int(input("Enter the number 3: "))

if number_1 > number_2:
    if number_1 > number_3:
        print("Number 1 is greater")
    else:
        print("Number 3 is greater")
elif number_2 > number_3:
    print("Number 2 is greater")
else:
    print("Number 3 is greater")



# using extra variable

# d=0
# if number_1>d:
#     d=number_1
# if number_2>d:
#     d=number_2
# if number_3>d:
#     d=number_3
# print(f"{d} is greater")


# using and operator

# if number_1>number_2 and number_1>number_3:
#     print("Number 1 is greater")
# elif number_2>number_1 and number_2>number_3:
#     print("Number 2 is greater")
# else:
#     print("Number 3 is greater")


 