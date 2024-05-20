# Develop a python program to create a class called as "FourthSem" with attributes like RollNum[20], Test1Marks[20], Test2Marks[20] and Test3Marks[20]. Calculate class average for each of the three tests for a class of 20 students. The program should also calculate the average of each of the student scores in those three tests and display. Display the top 5 and last 5 scores of the class for every test

import random
class FourthSem:

    def __init__(self, rollNums, test1Marks, test2Marks, test3Marks):
        self.rollNums = rollNums
        self.test1Marks = test1Marks
        self.test2Marks = test2Marks
        self.test3Marks = test3Marks

    def calculateClassAverage(self):
        t1 = sum(self.test1Marks)/20
        t2 = sum(self.test2Marks)/20
        t3 = sum(self.test3Marks)/20
        return t1, t2, t3

    def calculateStudentAverage(self,i):
        studentAverage = (self.test1Marks[i] + self.test2Marks[i] + self.test3Marks[i]) / 3
        return studentAverage

students = FourthSem([i+1 for i in range(20)], [random.randint(0,100) for j in range(20)], [random.randint(0,100) for k in range(20)], [random.randint(0,100) for l in range(20)])

for i in range(20):
    print(f"Student {i+1} average : {students.calculateStudentAverage(i):.2f}")

print(f"Class averages in three tests :{students.calculateClassAverage()}")