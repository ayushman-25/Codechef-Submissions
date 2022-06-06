a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a == b == c == d == 90):
    print("Rectangle")
elif (a == c and b == d):
    print("Parallelogram")
elif (a + b == 180 and c + d == 180):
    print("Trapezium")
elif (a + b + c + d == 360):
    print("Quadrilateral")
else:
    print("No Quadrilateral")
