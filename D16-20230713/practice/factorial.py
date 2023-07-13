def factorial():
    print("Finding factorial")
    number=int(input("Enter the number: "))
    fact = number * (number-1) * (number-2) * (number-3)
    return fact
print(factorial())