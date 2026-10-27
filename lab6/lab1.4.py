n = int(input())

if n < 0:
    print("Ошибка")
else:
    count = 0
    total_sum = 0
    temp = n
    
    if temp == 0:
        count = 1
        total_sum = 0
    else:
        while temp > 0:
            digit = temp % 10
            total_sum += digit
            count += 1
            temp //= 10
            
    print("Цифр:", count)
    print("Сумма цифр:", total_sum)
