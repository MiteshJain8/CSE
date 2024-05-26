import random
import time

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    j = high - 1
    while i<j:
        if(array[j]<pivot):
            i+=1
            array[i], array[j] = array[j], array[i]
        j-=1
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    while low < high:
        pi = partition(array, low, high)
        if pi - low < high - pi:
            quick_sort(array, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(array, pi + 1, high)
            high = pi - 1

arr = [random.randint(1,50000) for i in range(20000)]
N = len(arr)
start = time.time()
quick_sort(arr, 0, N - 1)
end = time.time()
print(end-start)