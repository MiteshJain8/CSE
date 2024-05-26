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

arr = [random.randint(1,50000) for i in range(20000)]
start = time.time()
merge_sort(arr)
end = time.time()
print(end-start)