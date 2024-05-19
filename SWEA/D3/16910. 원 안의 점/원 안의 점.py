t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cnt = 0
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if x ** 2 + y ** 2 <= n ** 2:
                cnt += 1
    print(f'#{tc} {cnt}')
