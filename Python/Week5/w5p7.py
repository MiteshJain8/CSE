# Develop a python program to read convert a date of yyyy-mm-dd format to dd-mm-yyyy format

from datetime import datetime

date = input("Enter date in yyyy-mm-dd format: ")
date_obj = datetime.strptime(date, '%Y-%m-%d')
format_date = date_obj.strftime('%d-%m-%Y')
print("Date in dd-mm-yyyy format:", format_date)