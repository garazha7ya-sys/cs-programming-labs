
data = input().split()
original = [int(x) for x in data]

corrected = original[:]

for i in range(len(corrected)):
    if corrected[i] < 0:
        corrected[i] = 0

print(f"Исходные остатки: {original}")
print(f"Исправленные остатки: {corrected}")
