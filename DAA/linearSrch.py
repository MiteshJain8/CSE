import time
strt = time.time()
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

list = [5, 2, 8, 12, 1, 3, 4, 6, 7, 9, 10, 11, 13, 14, 15]
print(linear_search(list, 15))
end = time.time()
print(end-strt)