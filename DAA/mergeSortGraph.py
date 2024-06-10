import matplotlib.pyplot as plt
import math as mh
import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])
        i=0
        j=0
        k=0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

def mergeTime(x):
    arr = [random.randint(1,90000) for i in range(x)]
    start = time.time()
    merge_sort(arr)
    end = time.time()
    return end-start

merge = lambda x: mergeTime(x)
xpts = [x for x in range(100,10000,100)]
plt.plot(xpts, [merge(x) for x in xpts])
plt.xlabel('Array Size')
plt.ylabel('Time')
plt.show()