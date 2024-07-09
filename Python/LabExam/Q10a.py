# Develop a python program to demonstrate handling of following exceptions using try and except. 
# NameError 
# IndexError 
# KeyError 
# ZeroDivisionError 

try:
    print(unknown_variable) # type: ignore
except NameError as e:
    print(f"NameError caught: {e}")

try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"IndexError caught: {e}")

try:
    d = {'a': 1, 'b': 2}
    print(d['c'])
except KeyError as e:
    print(f"KeyError caught: {e}")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError caught: {e}")