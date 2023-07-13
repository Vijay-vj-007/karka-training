month=(int(input("Enter the number between 1 and 12: ")))
def month_name(months):
    if months == 1:
        return "JANUARY"
    elif months == 2:
        return "FEBRUARY"
    elif months == 3:
        return "MARCH"
    elif months == 4:
        return "APRIL"
    elif months == 5:
        return "MAY"
    elif months == 6:
        return "JUNE"
    elif months == 7:
        return "JULY"
    elif months == 8:
        return "AUGUST"
    elif months == 9:
        return "SEPTEMBER"
    elif months == 10:
        return "OCTOBER"
    elif months == 11:
        return "NOVEMBER"
    elif months == 12:
        return "DECEMBER"
    else:
        return "choose between 1 and 12"
    
print(month_name(month))    


    