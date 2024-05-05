# 6.	Create a findQuadraticRoots() function that finds the roots of a quadratic equation. Display appropriate messages

import cmath

def findQuadraticRoots(a, b, c):
    d = (b**2) - (4*a*c)

    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)

    print("The solutions are ",root1," and ",root2)

print("For ax^2 + bx + c = 0 , enter a, b and c:")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
findQuadraticRoots(a, b, c)