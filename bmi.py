w = float(input())
h = float(input())

bmi = w/(h**2)
print(round(bmi, 1))
if bmi < 20:
    print("nguoi gay")
elif 20 <= bmi <= 30:
    print("nguoi li tuong")
else:
    print("nguoi beo")
