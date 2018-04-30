#Caleb Callaway
#3/27/18
#displayDate.py - prints out the date


from datetime import date
from calendar import weekday


day = date.today().day
month = date.today().month
year = date.today().year

print (weekdays[weekday(year,month,day)])

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]