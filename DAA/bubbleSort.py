import time
import random
def bubble_sort(arr,n):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

list = [random.randint(1,50000) for i in range(20000)]
n = len(list)
start = time.time()
sorted_list = bubble_sort(list,n)
end = time.time()
print(end-start)