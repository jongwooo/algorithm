import sys

n, k, p = map(int, sys.stdin.readline().split())
breads = list(map(int, sys.stdin.readline().split()))
available = 0
for i in range(n):
    cnt = 0
    for j in range(k):
        if breads[i * k + j] == 0:
            cnt += 1
    if cnt < p:
        available += 1
print(available)
