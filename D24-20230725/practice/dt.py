# from datetime import date

# my_date=date(2023,7,25)
# my_date=date.today()

# print(my_date)


# from datetime import datetime
# my_time=datetime.now()
# b=my_time.strftime("%M")
# print(b)

# from datetime import datetime

# import pytz

# ist=pytz.timezone("America/New_York")

# print(datetime.now(ist))

#timedelta to add or subract days
from datetime import datetime,timedelta


date_str="24 December 2023"
c=datetime.strptime(date_str,"%d %B %Y")
d=c+timedelta(days=5)
print(d)


from dateutil import parser
 
DT = parser.parse("Jun 23 2022 07:31PM")
 
print(DT)
