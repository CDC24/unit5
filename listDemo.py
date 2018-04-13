#Caleb Callaway
#4/13/18
#listDemo.py - print out 1st and last word in a list



words = input("Enter some words please: ").split(" ")

print("The first word was",words[0])
print("The last word was",words[-1])


#print list one item at a time

for item in words:
    print (item)