import sys


def input():
    return sys.stdin.readline()


n, m = map(int, input().split())
tasteless = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    tasteless[i][j] = tasteless[j][i] = True
cnt = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if tasteless[i][j] or tasteless[j][k] or tasteless[i][k]:
                continue
            cnt += 1
print(cnt)
