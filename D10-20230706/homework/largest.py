# numbers=[1,100,300,4]

# numbers1=[2,400,500,3]


def find_largest(numbers):
    largest=0
    for number in numbers:
        if number > largest:
            largest = number
    return largest


# result=find_largest(numbers)
# print("The Largest Number = ", result)

# r1=find_largest(numbers1)
# print("largest number=",r1)
 
    
