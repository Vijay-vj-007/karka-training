def bmi():
    height=float(input("Enter your height in m : "))
    weight=float(input("Enter your weight in kg : "))
    BMI=weight/(height*height)
    if BMI < 18.5:
        return f"Your BMI is {BMI}\nBMI Category: Underweight"
    elif (BMI >=18.5) and (BMI<=24.9):
        return f"Your BMI is {BMI}\nBMI Category: Normal weight"
    elif (BMI >=25) and (BMI <=29.9):
        return f"Your BMI is {BMI}\nBMI Categoty: Over weight"
    elif BMI >= 30:
        return f"Your BMI is {BMI}\nBMI Categoty: Obese"
    else:
        return "choose between Height and Weight"
print(bmi())
