#Caleb Callaway
#5/2/18
#quicksortPseudocode.py - using Wikipedia pseudocode for quicksort

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def quickSort(A, low, high):
    if low < high:
        p = partition (A, low, high)
        quickSort(A, low, p-1 )         #repeating on either side of partition
        quickSort(A, p+1, high)
    return A

def partition(A, low, high):
    pivot = A[high]
    i = low-1
    for j in range (low, high):        #splitting
        if A[j]<pivot:
            i +=1
            A[i],A[j] = A[j],A[i]       #rearranging
    A[i+1], A[high] = A[high], A[i+1]
    return i+1
    
if __name__ == '__main__':

     #make a list of N random numbers between 1 and N
    A = [0]*N
    for q in range(N):
        A[q] = randint(1,N)
    
    pythonSort = sorted(A) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    A = quickSort(A, 0, N-1)
    #numbers = numbers.sort()       #tested the python sort
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(A == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
