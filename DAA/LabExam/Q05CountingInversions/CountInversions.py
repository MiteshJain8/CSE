def merge_and_count(left_arr, right_arr):
    merged = []
    i, j = 0, 0
    inversions = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
            inversions += len(left_arr) - i  # Count inversions
    
    # Append any remaining elements from left and right halves
    merged += left_arr[i:]
    merged += right_arr[j:]
    return merged, inversions

def mergeSort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_inversions = mergeSort_and_count(arr[:mid])
    right_half, right_inversions = mergeSort_and_count(arr[mid:])
    merged, merge_inversions = merge_and_count(left_half, right_half)
    
    total_inversions = left_inversions + right_inversions + merge_inversions
    return merged, total_inversions

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
sorted_arr, inversion_count = mergeSort_and_count(arr)
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversion_count)