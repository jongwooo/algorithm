t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    result = []
    for i in range(n - k + 1):
        for x in range(i + k - 1, n):
            result.append(a[x] - a[i])
    print(f'#{tc} {min(result)}')
