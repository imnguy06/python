from math import sqrt

a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c

if d < 0:
    print("PTVN")
else:
    x1 = (-b - sqrt(d))/(2*a)
    x2 = -b/a - x1
    print(int(x2), int(x1))
