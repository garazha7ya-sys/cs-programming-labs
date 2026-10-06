
current = float(input().replace(',', '.'))

target = float(input().replace(',', '.'))

# Проверяем условия
if current > target:
    print("Охлаждение")
elif current < target:
    print("Нагрев")
else:
    print("Выключен")