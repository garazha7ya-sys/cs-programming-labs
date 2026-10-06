data = input()

parts = data.split(';')

train_number = parts[0]
from_city = parts[1]
to_city = parts[2]
departure_time = parts[3]
price = float(parts[4])

print(f"Поезд: {train_number}")
print(f"Маршрут: {from_city} - {to_city}")
print(f"Отправление: {departure_time}")
print(f"Цена: {price:.2f} руб")