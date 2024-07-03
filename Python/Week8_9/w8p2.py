import numpy as np

lst = list(map(int, input(f"Enter 12 elements separated by space: ").split()))
if len(lst) != 12:
    raise Exception(f"Enter exactly 12 elements.")
arr = np.array(lst).reshape(3, 4)
print("2D Array:\n", arr)

print("Array in reverse order using slicing:\n", arr[::-1, ::-1])
print("Array in reverse order using for loop:")
for row in arr[::-1]:
    for ele in row[::-1]:
        print(ele, end=' ')
    print()

print("Sum of all elements:", np.sum(arr))
print("Principal diagonal elements:", np.diagonal(arr))

arr_1d = arr.flatten()
arr_3d = arr.reshape(2, 3, 2)
print("1D Array:\n", arr_1d)
print("3D Array:\n", arr_3d)

sort_asc = np.sort(arr, axis=None).reshape(arr.shape)
sort_desc = np.sort(arr, axis=None)[::-1].reshape(arr.shape)
print("2D Array sorted in ascending order:\n", sort_asc)
print("2D Array sorted in descending order:\n", sort_desc)