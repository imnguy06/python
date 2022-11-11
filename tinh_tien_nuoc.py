n = int(input())

if n < 10:
    t = n*4000
else:
    t = 10*4000+(n-10)*7000
print(t)
