number_1=int(input("enter the number : "))
operator=input("enter the operator ( +,-,*,/,%,**) : ")
number_2=int(input("enter the number : "))

def operation(number_1,operator,number_2):
    if operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "*":
        return number_1 * number_2
    elif operator == "/":
        return number_1 / number_2
    elif operator == "%":
        return number_1 % number_2
    elif operator == "**":
        return number_1 ** number_2
    else:
        return "no operator found"
result=operation(number_1,operator,number_2)
print(result)
