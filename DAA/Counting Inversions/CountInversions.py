def merge_and_count(arr, left, mid, right):
    temp_arr = arr[left:right + 1]
    i, j, k, inv_count = 0, mid - left + 1, left, 0

    while i <= mid - left and j < len(temp_arr):
        if temp_arr[i] <= temp_arr[j]:
            arr[k] = temp_arr[i]
            i += 1
        else:
            arr[k] = temp_arr[j]
            inv_count += (mid - left + 1 - i)
            j += 1
        k += 1

    while i <= mid - left:
        arr[k] = temp_arr[i]
        i += 1
        k += 1

    while j < len(temp_arr):
        arr[k] = temp_arr[j]
        j += 1
        k += 1

    return inv_count

def sort_and_count(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = sort_and_count(arr, left, mid)
    inv_count += sort_and_count(arr, mid + 1, right)
    inv_count += merge_and_count(arr, left, mid, right)

    return inv_count

arr = [21, 16, 22, 15, 24, 32, 12, 14, 27, 11]
result = sort_and_count(arr, 0, len(arr) - 1)
print("Number of inversions are", result)