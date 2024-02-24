import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
c = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(k):
        for z in range(m):
            c[x][y] += a[x][z] * b[z][y]
for i in c:
    print(*i)
