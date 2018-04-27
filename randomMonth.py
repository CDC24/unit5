#Caleb Callaway
#3/27/18
#randomMonth.py - prints a random month


from random import randint

Months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

select = randint(0,11)

print (Months[select])
