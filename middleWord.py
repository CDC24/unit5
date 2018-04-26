#Caleb Callaway
#3/25/18
#middleWord.py - prints the middle word in a list

w = input("enter some words: ")


words = w.split(" ")

if len(words)%2==0:
    print(words[len(words)/2],words[(len(words)/2)-1])
else:
    print (words[len(words)/2])    