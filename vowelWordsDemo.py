#Caleb Callaway
#3/26/18
#vowelWordsDemo.py- using strings like lists- tells if str starts with a vowel

words = (input("Words please: ")).split(" ")

for word in words:
    if word[0] in "AEIOUaeiou":
        print (word)