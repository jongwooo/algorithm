n = int(input())
count = 0
while n > 0:
    if n % 5 == 0:
        count += n // 5
        break
    if n - 2 < 0:
        count = -1
        break
    n -= 2
    count += 1
print(count)
