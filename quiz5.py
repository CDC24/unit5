#Caleb Callaway
#5/7/18
#quiz5.py - lists quiz



def penultimate(list):
    return (list[-2])
    
def plusEquals(list,num):
    for i in range (0, len(list)):
        list[i]+=num
    return (list)
    
def smallest(list):
    small = list[0]
    for num in list:
        if num< small:
            small = num
    return (small)
    
def decimalRange(a,b,c):
    R = [a]
     length = (b-a)/c
    for i in range (0,length):
        R.append(R[i-1]+c)
    
    
    
    
#testing

L = ["peanut", "butter", "jelly", "time"]

print(penultimate(L))

N = [3,6,12,78,2,10]

print(smallest(N))

print(plusEquals(N,4))

print (decimalRange(4,10,0.5))