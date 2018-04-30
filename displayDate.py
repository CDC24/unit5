#Caleb Callaway
#3/27/18
#displayDate.py - prints out the date


from datetime import date
from calendar import weekday


day = date.today().day
month = date.today().month
year = date.today().year

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]


print ("Today is",weekdays[weekday(year,month,day)],",", months[month-1], day)

