# Write a python program to read 2 numbers from the keyboard and perform the basic arithmetic operations based on the choice. (1-Add, 2-Subtract, 3-Multiply, 4-Divide)

def operate(num1, num2, choice):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid choice."

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Enter the operation you want to perform:")
print("1-Add, 2-Subtract, 3-Multiply, 4-Divide")
choice = int(input())

print("Result:", operate(num1, num2, choice))