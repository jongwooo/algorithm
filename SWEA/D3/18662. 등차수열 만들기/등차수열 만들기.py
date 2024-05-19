t = int(input())
for tc in range(1, t + 1):
    a, b, c = map(int, input().split())
    x = 0.0
    if b - a != c - b:
        x = abs((b - a) - (c - b)) / 2
    print(f'#{tc} {x}')
