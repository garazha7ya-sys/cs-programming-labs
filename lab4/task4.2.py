price = float(input().replace(',', '.'))
age = int(input())

if price <= 0 or age < 0 or age > 128:
    print("Ошибка")
else:
    if age <= 5:
        cost = price * 0
    elif age <= 17:
        cost = price * 0.5
    elif age <= 59:
        cost = price * 1.0
    else:
        cost = price * 0.7
    print(f"Стоимость: {cost:.2f} руб")