import math
import sys

n, k = map(int, sys.stdin.readline().split())
m = [0] * 6
f = [0] * 6
for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())
    if s == 0:
        m[y - 1] += 1
    else:
        f[y - 1] += 1
cnt = 0
for i in range(6):
    cnt += math.ceil(m[i] / k)
for i in range(6):
    cnt += math.ceil(f[i] / k)
print(cnt)
