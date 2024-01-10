n = int(input())
result = [1, 2] * (n // 2)
if n % 2 != 0:
    result += [3]
print(*result)
