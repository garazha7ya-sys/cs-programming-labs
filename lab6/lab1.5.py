n = int(input())

if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        for j in range(n):
            if i > j:
                dist = i - j
            else:
                dist = j - i
            
            print(dist, end="")
            if j < n - 1:
                print(" ", end="")
        print()
