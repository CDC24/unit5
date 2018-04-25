#Caleb Callaway
#3/25/18
#warmUp13.py - list 20 random numbers, prints sum, prints minimum, prints max

from random import randint

nums = []

for i in range (0,20):
    nums.append(randint(1,100))

print(sum(nums))
print(min(nums))
print(max(nums))