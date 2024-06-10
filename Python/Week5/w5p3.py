# Develop a python program to read an USN and check if the USN starts with "1MS" and ends with "0". The length of the USN must be strictly 10. Display the appropriate results.

import re

USN = input("Enter the USN: ")
if(re.match('^1MS.{6}0$', USN)):
    print("Valid")
else:
    print("Invalid")