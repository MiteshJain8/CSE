# Write a python function binarySearch() to read a sorted array and search for the key element. Display the appropriate messages

def binSearch(arr,start,end,key):
    if(start<=end):
        mid = (start+end)//2
        if(arr[mid]==key):
            return mid+1
        elif(arr[mid]>key):
            return binSearch(arr,start,mid-1,key)
        else:
            return binSearch(arr,mid+1,end,key)
    else:
        return -1

n = int(input("Enter the number of elements: "))
print("Enter the sorted elements:")
arr = [int(input()) for i in range(n)]
key = int(input("Enter the key: "))
ans = binSearch(arr,0,n-1,key)
if(ans==-1):
    print("Key not found")
else:
    print("Key found at position",ans)