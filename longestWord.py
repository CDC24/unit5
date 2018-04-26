#Caleb Callaway
#3/25/18
#longestWord.py - prints the longest word in a list


words = input("enter some words: ").split(" ")

  
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)