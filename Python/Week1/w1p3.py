# 3.	Write a python program to read 4 subject marks and display grades. (91-100: S Grade, 81-90: A Grade, 71-80: B Grade, 61-70: C Grade, 51-60: D Grade, 41-50: E Grade, 00-40: F Grade).

def calculate_grade(mark):
    if 91 <= mark <= 100:
        return 'S Grade'
    elif 81 <= mark <= 90:
        return 'A Grade'
    elif 71 <= mark <= 80:
        return 'B Grade'
    elif 61 <= mark <= 70:
        return 'C Grade'
    elif 51 <= mark <= 60:
        return 'D Grade'
    elif 41 <= mark <= 50:
        return 'E Grade'
    elif 0 <= mark <= 40:
        return 'F Grade'
    else:
        return 'Invalid mark'

marks = []
for i in range(1, 5):
    mark = float(input(f"Enter the mark for subject {i}: "))
    marks.append(mark)

for i, mark in enumerate(marks, start=1):
    grade = calculate_grade(mark)
    print(f"The grade for subject {i} is: {grade}")
