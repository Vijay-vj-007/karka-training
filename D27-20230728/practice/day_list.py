days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
total_days = 30

day_list = []

for i in range(len(days)):
    a=[]
    for j in range(i+1,total_days+1,len(days)):
        a.append(j)
    week ={"day":days[i],"days_list":a}
    day_list.append(week)

print(day_list)
    
