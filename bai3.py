import math

a = float(input())
b = float(input())
c = float(input())
cv = a + b + c
p = cv / 2
s = math.sqrt(p*(p - a)*(p - b)*(p - c))

print(cv)
print(round(s, 1))
