import math

def quadraticEquation():
    a = float(input("a equals to:"))
    b = float(input("b equals to:"))
    c = float(input("c equals to:"))

    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print("Two real roots are: " +  str(x1) + " and " + str(x2))

    elif d == 0:
        x = (-b)/(2*a)
        print("The only real root is: " + str(x))
    else:
        print("discriminant is less than 0")
quadraticEquation()