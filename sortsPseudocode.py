#Caleb Callaway
#5/2/18
#sortsPseudocode.py - using Wikipedia pseudocode

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def quickSort(A, 0, N-1):
    if 0 < N-1:
        p = partion (A, 0, N-1)
        quickSort(A, 0, p-1 )
        quickSort(A, p+1, N-1)

def partition:
    pivot = A[N-1]
    i = low-1
    
    
    
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
