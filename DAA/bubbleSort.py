import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

strt = time.time()
my_list = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(sorted_list)
end = time.time()
print(end-strt)