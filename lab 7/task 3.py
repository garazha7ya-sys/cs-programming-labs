
input_str = input()
numbers = list(map(int, input_str.split())) if input_str.strip() else []

target = int(input())

indices = [i for i, x in enumerate(numbers) if x == target]

print(f"Индексы: {indices}")