import math

a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = math.sqrt(p*(p - a)*(p - b)*(p - c))

print(round(p * 2, 1))
print(round(s, 1))

#có thể dùng 2 hàm này cũng được
#print('{:.1f}'.format(p * 2))
#print('{:.1f}'.format(s))

