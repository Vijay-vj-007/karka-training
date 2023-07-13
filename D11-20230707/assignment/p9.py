def week_day(day_number):
    if day_number == 0:
        return "SATURDAY"
    elif day_number == 1:
        return "SUNDAY"
    elif day_number == 2:
        return "MONDAY"
    elif day_number == 3:
        return "TUESDAY"
    elif day_number == 4:
        return "WEDNESDAY"
    elif day_number == 5:
        return "THURSDAY"
    elif day_number == 6:
        return "FRIDAY"
    elif day_number == 7:
        return "SATURDAY"
    else:
        return "ERROR"
    
a=week_day(int(input("Enter the week day : ")))
if a == "ERROR":
    print("ERROR") 
else:
    print("Today is a",a)






