n = int(input())
result = 0
for i in range((n // 5) + 1):
    for j in range((n // 3) + 1):
        if 5 * i + 3 * j == n:
            result = i + j
print(result if result else -1)
