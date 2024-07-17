import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
turns = [0] * (min(n, m) // 2)
for i in range(min(n, m) // 2):
    turns[i] = 2 * ((n - (2 * i)) + (m - (2 * i))) - 4
for i in range(min(n, m) // 2):
    for r in range(k % turns[i]):
        temp = arr[i][i]
        for j in range(1 + i, m - i):
            arr[i][j - 1] = arr[i][j]
        for j in range(1 + i, n - i):
            arr[j - 1][m - 1 - i] = arr[j][m - 1 - i]
        for j in range(1 + i, m - i):
            arr[n - 1 - i][m - j] = arr[n - 1 - i][m - 1 - j]
        for j in range(1 + i, n - i):
            arr[n - j][i] = arr[n - 1 - j][i]
        arr[1 + i][i] = temp
for a in arr:
    print(*a)
