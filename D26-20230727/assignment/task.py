# from datetime import datetime,timedelta
# day = int(input("Enter days: "))
# date = "27 July 2023"
# c = datetime.strptime(date, "%d %B %Y")
# d = c + timedelta(days=day)
# e= d.strftime("%d %B %Y")
# print(e)

from datetime import datetime,timedelta
day = int(input("Enter days: "))
date =input("enter date month year in (DD MM YY): ")
c = datetime.strptime(date, "%d %B %Y")
d = c - timedelta(days=day)
e= d.strftime("%d %B %Y")
print(e)
