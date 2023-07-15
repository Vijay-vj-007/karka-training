year=int(input("enter the year : "))

def check_eligibility(year):
    if (year >= 2021):
        return "you are eligible"
    else:
        return "you are not eligible"
result=check_eligibility(year)
print(result)
