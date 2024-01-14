n = int(input())
cnt = 1
temp = 1
while n > temp:
    temp += 6 * cnt
    cnt += 1
print(cnt)
