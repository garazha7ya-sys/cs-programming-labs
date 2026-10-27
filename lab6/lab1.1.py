a = int(input())
b = int(input())

if a < 0 or b < 0 or (a == 0 and b == 0):
    print("Ошибка")
else:
    while b > 0:
        a, b = b, a % b
    print("НОД:", a)
