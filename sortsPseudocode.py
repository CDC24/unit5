#Caleb Callaway
#5/2/18
#sortsPseudocode.py - using Wikipedia pseudocode

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range (0,len(A)-1):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i] #python swappin'
                swapped = True
        if not swapped:
            break
        for i in range (len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1],A[i] #python swappin'
                swapped = True
    
    return A
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    #numbers = numbers.sort()       #tested the python sort
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
