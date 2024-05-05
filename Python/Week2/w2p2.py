# 2.	Create a displayMinMax() function that takes an Array and  displays the maximum and minimum number from the array. Create a displaySecondMax() to display the second largest number from the array without sorting

def dispMinMax(arr):
    k = len(arr)
    maxi = arr[0]
    mini = arr[0]
    for i in range(1,k):
        if(arr[i]>maxi):
            maxi = arr[i]
        if(arr[i]<mini):
            mini = arr[i]
    print("Max = ",maxi)
    print("Min = ",mini)

def dispSecMax(arr):
    k = len(arr)
    secMax = arr[0]
    maxi = arr[0]
    for i in range(1,k):
        if(arr[i]>maxi):
            maxi = arr[i]
    for i in range(1,k):
        if(arr[i]>secMax and arr[i]<maxi):
            secMax = arr[i]
    print("Second largest = ",secMax)

arr = []
n = int(input("Enter number of elements:"))
print("Enter the elements:")
for i in range(n):
    x = int(input())
    arr.append(x)
dispMinMax(arr)
dispSecMax(arr)