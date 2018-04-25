#Caleb Callaway
#3/25/18
#dictionaryDemo.py - list practice

words = ["computer", "mortify", "dog", "firetruck", "yes", "python", "cat"]

words.sort()

num = int(input("what number word do you want?  "))
if num<=0 or num >=len(words)+1:
    print("you can't have that")
else:
    print(words[num-1])