n = int(input())

if n < 2:
    print("Ошибка")
else:
    d = 2
    first = True
    while n > 1:
        if n % d == 0:
            if not first:
                print(" ", end="")
            print(d, end="")
            n //= d
            first = False
        else:
            d += 1 
    print()
