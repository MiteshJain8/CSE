import time
import random
def insertion_sort(arr,n):
    for i in range(1,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr

list = [random.randint(1,50000) for i in range(20000)]
arr = [12, 11, 13, 5, 6] 
n = len(arr)
start = time.time()
sorted_list = insertion_sort(arr,n)
end = time.time()
print(end-start)
print(sorted_list)