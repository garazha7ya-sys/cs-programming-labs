a = int(input())
b = int(input())

summa = 0
proizvedenie = 1

for i in range(a, b + 1):
    summa += i
    proizvedenie *= i

print(f"Сумма: {summa}")
print(f"Произведение: {proizvedenie}")