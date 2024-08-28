# Write  a  python  program  to  perform  the  following  operations  using  user defined functions 
# Display the maximum and minimum number from the array. 
# Display  the  second  largest  number  from  the  array  without sorting

def displayMinMax(arr, n):
    Max = arr[0]
    Min = arr[0]
    for i in range(1,n):
        if(arr[i]>Max):
            Max = arr[i]
        if(arr[i]<Min):
            Min = arr[i]
    print(f"Max = {Max}, Min = {Min}")
    return Max, Min

def displaySecMax(arr, n, Max, Min):
    secMax = Min
    for i in range(n):
        if(arr[i]>secMax and arr[i]<Max):
            secMax = arr[i]
    print("Second largest = ",secMax)

n = int(input("Enter number of elements: "))
print("Enter the elements:")
arr = [int(input()) for i in range(n)]
Max, Min = displayMinMax(arr, n)
displaySecMax(arr, n, Max, Min)