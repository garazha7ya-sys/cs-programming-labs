count = 0
total_cost = 0

while True:
    value = input()
    if value == "stop":
        break
    cost = int(value)
    count += 1
    total_cost += cost

if count == 0:
    print("Нет покупок")
else:
    average = total_cost / count
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total_cost} руб")
    print(f"Средняя стоимость: {average:.2f} руб")