a, b = map(int, input().split())
cnt = 1
while a != b:
    if a > b:
        cnt = -1
        break
    elif str(b)[-1] == '1':
        b //= 10
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)
