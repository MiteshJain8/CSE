def merge_and_count(arr, left, mid, right):
    temp_arr = []
    i, j, inv_count = left, mid + 1, 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr.append(arr[i])
            i += 1
        else:
            temp_arr.append(arr[j])
            inv_count += (mid - i + 1)
            j += 1

    while i <= mid:
        temp_arr.append(arr[i])
        i += 1

    while j <= right:
        temp_arr.append(arr[j])
        j += 1

    for k in range(len(temp_arr)):
        arr[left + k] = temp_arr[k]

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