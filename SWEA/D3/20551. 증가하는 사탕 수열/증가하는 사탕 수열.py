t = int(input())
for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    cnt = 0
    if b >= c:
        cnt += b - c + 1
        b = c - 1
    if a >= b:
        cnt += a - b + 1
        a = b - 1
    if a < 1 or b < 1 or c < 1:
        cnt = -1
    print(f'#{tc} {cnt}')
