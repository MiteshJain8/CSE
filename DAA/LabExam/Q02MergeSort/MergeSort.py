def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements from left and right halves
    merged += left[i:]
    merged += right[j:]
    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])
    return merge(left_half, right_half)

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = mergeSort(arr)
print("Sorted array:", sorted_arr)