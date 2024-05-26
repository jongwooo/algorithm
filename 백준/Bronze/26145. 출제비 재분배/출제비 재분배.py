import sys

n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
result = s + [0] * m
for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    for j in range(n + m):
        result[i] -= t[j]
        result[j] += t[j]
print(*result)
