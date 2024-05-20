# Develop a python program to create a class called as "Shape" and subclasses as “Rectangle” and “Triangle” with following data members like side1 and side2 and methods like calculateArea() and displayDetails(). Write the necessary constructors and test for different cases

class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def calculateArea(self):
        area = self.side1 * self.side2
        return area

    def displayDetails(self):
        print("Side 1:", self.side1)
        print("Side 2:", self.side2)

class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

    def displayDetails(self):
        print("Rectangle:")
        super().displayDetails()
        self.area = self.calculateArea()
        print("Area:", self.area)
        print()

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2)
        self.side3 = side3

    def calculateArea(self):
        a = self.side1
        b = self.side2
        c = self.side3
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**(0.5)
        return area
    
    def displayDetails(self):
        print("Triangle:")
        super().displayDetails()
        print("Side 3:",self.side3)
        self.area = self.calculateArea()
        print("Area:", self.area)

r = Rectangle(10, 20)
t = Triangle(3, 4, 5)
r.displayDetails()
t.displayDetails()