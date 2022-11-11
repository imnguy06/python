a = int(input())
check = 0

for i in range(1, a+1):
    if i**2 == a:
        check = 1
        break

if check == 1:
    print("Yes")
else:
    print("No")
