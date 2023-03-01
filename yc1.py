n = int(input("Nhập số phần tử của dãy số: "))
a = []
for i in range(n):
    a.append(int(input("Nhập phần tử thứ {} của dãy số: ".format(i+1))))

if n % 2 == 1:
    mid = n // 2
    del a[mid]

print("Dãy số sau khi xóa:")
for x in a:
    print(x, end=" ")
