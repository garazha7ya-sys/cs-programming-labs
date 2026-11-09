nums = list(map(int, input().split()))

squares = [x**2 for x in nums if x > 0 and x % 2 != 0]

print("Квадраты:", squares)
