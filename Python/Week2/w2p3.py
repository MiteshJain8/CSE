# 3.	Write a python function linearSearch() to read an array and search for the key element. Display the appropriate messages. Use the recursive function

def linearSearch(arr, index, key):
    if index < len(arr):
        if arr[index] == key:
            return index+1
        else:
            return linearSearch(arr, index + 1, key)
    else:
        return -1

arr = []
n = int(input("Enter the number of elements: "))
print("Enter the ",n," elements:")
for i in range(n):
    x = int(input())
    arr.append(x)
key = int(input("Enter the key: "))
ans = linearSearch(arr, 0, key)
if(ans==-1):
    print("Key not found")
else:
    print("Key found at position",ans)