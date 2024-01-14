n = int(input())
cnt = 0
for i in range(n):
    temp = i * (i + 1) // 2
    if n <= temp:
        break
    if (n - temp) % (i + 1) == 0:
        cnt += 1
print(cnt)
