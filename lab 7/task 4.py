
r, c = map(int, input().split())

matrix = []
for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

row_sums = []
for i in range(r):
    row_sum = 0
    for j in range(c):
        row_sum += matrix[i][j]
    row_sums.append(row_sum)

col_sums = []
for j in range(c):
    col_sum = 0
    for i in range(r):
        col_sum += matrix[i][j]
    col_sums.append(col_sum)

print(f"Суммы строк: {row_sums}")
print(f"Суммы столбцов: {col_sums}")