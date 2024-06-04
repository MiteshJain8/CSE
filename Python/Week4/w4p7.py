# Develop a python program to create a class called as Quadratic. Write the constructor to initialize the necessary variables. Find the roots of a quadratic equation and test for all the conditions

import cmath
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def find_roots(self):
        d = (self.b**2) - (4*self.a*self.c)
        root1 = (-self.b + cmath.sqrt(d)) / (2*self.a)
        root2 = (-self.b - cmath.sqrt(d)) / (2*self.a)
        print("Two roots are {:.2f} and {:.2f}".format(root1, root2))

q = Quadratic(1, 5, 7)
q.find_roots()