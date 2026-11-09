r, c = map(int, input().split())

matrix = []
for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

row_start, row_end, col_start, col_end = map(int, input().split())

target = int(input())

found = False

for i in range(row_start, row_end + 1):
    for j in range(col_start, col_end + 1):
        if matrix[i][j] == target:
            print(f"{i} {j}")
            found = True

if not found:
    print("Не найдено")