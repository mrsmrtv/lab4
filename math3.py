import math
n=int(input("How many sides: "))
l=int(input("Length of 1 side: "))

print("Area of the polygon= ", n*(l**2)/4*math.tan(math.pi/n))