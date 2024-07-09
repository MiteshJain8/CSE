# Write  a  python  program  to  utilize  NumPy  and  perform  the  following operations. 
# Read and display a 2D Array. 
# Display the array elements in the reverse order. 
# Display all the elements of principal diagonal elements. 
# Sort the 2D array in ascending and descending order

import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter array elements:")
lst = [int(input()) for i in range(rows * cols)]
arr = np.array(lst).reshape(rows, cols)
print("Original Array:")
print(arr)

print("Array elements in reverse order:")
print(arr[::-1, ::-1])

print("Principal diagonal elements:",np.diagonal(arr))

sorted_arr = np.sort(arr, axis=None).reshape(arr.shape)
print("Array sorted in ascending order:")
print(sorted_arr)

sorted_arr = np.sort(arr, axis=None)[::-1].reshape(arr.shape)
print("Array sorted in descending order:")
print(sorted_arr)