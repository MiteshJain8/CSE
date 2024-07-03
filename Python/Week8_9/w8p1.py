import numpy as np

arr1 = np.array([int(x) for x in input("Enter array elements separated by space: ").split()])
print("1D Array:", arr1)

arr2 = np.array([int(x) for x in input("Enter second array elements separated by space: ").split()])
common = np.intersect1d(arr1, arr2)
print("Common elements:", common)

arr = np.array([int(x) for x in input("Enter 12 elements separated by space: ").split()])
if arr.size != 12:
    raise Exception("Enter exactly 12 elements.")
arr_2x6 = arr.reshape(2, 6)
arr_3x4 = arr.reshape(3, 4)
arr_3d = arr.reshape(2, 3, 2)
print("2D Array (2x6):\n", arr_2x6)
print("2D Array (3x4):\n", arr_3x4)
print("3D Array:\n", arr_3d)

arr_split_2 = np.array_split(arr, 2)
arr_split_3 = np.array_split(arr, 3)
arr_split_4 = np.array_split(arr, 4)
print("Split into 2 arrays:\n", arr_split_2)
print("Split into 3 arrays:\n", arr_split_3)
print("Split into 4 arrays:\n", arr_split_4)

concatenated = np.concatenate((arr1, arr2))
print("Concatenated Array:", concatenated)

sort_asc = np.sort(arr)
sort_des = np.sort(arr)[::-1]
print("Array sorted in ascending order:", sort_asc)
print("Array sorted in descending order:", sort_des)

even_nums = arr[arr % 2 == 0]
print("Even numbers in the array:", even_nums)