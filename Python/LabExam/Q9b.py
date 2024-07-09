# Develop a python program to demonstrate handling multiple exceptions using try, except, else and finally block statements

try:
    operation = int(input("Choose an operation (1 for NameError, 2 for IndexError, 3 for KeyError, 4 for ZeroDivisionError, 5 for No Error): "))

    if operation == 1:
        print(unknown_variable) # type: ignore
    elif operation == 2:
        lst = [1, 2, 3]
        print(lst[10])
    elif operation == 3:
        d = {'a': 1, 'b': 2}
        print(d['c'])
    elif operation == 4:
        result = 10 / 0
    elif operation == 5:
        print("No errors here!")
    else:
        print("Invalid selection")

except NameError as e:
    print(f"NameError caught: {e}")
except IndexError as e:
    print(f"IndexError caught: {e}")
except KeyError as e:
    print(f"KeyError caught: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("The operation was successful!")
finally:
    print("This is finally block.")