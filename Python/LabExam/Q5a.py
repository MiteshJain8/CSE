# Write  a  python  program  to  create  a  tuple  and  perform  the  following operations    
# Adding an items 
# Displaying the length of the tuple 
# Checking for an item in the tuple 
# Accessing an items

tup = tuple()

n = int(input("Enter number of items to add: "))
for i in range(n):
    item = input(f"Enter item {i+1}: ")
    tup += (item,)

print(f"Length of tuple: {len(tup)}")

check = input("Enter item to check: ")
if check in tup:
    print(f"{check} is present in the tuple")
else:
    print(f"{check} is not present in the tuple")

index = int(input("Enter index of item to access: "))
if index < len(tup):
    print(f"Item at index {index} is {tup[index]}")
else:
    print("Index out of range")