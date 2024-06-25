# Develop a python program to read 5 integer values from the keyboard. Display the sum and average of these numbers. If the user enters any other value, then raise the ValueError exception. Display appropriate messages

try:
    nums = []
    for i in range(5):
        nums.append(int(input(f"Value {i+1}: ")))
    Sum = sum(nums)
    avg = Sum / len(nums)
    print(f"\nSum = {Sum}\nAverage = {avg:.2f}")

except ValueError:
    print("Invalid input! Please enter an integer value.")