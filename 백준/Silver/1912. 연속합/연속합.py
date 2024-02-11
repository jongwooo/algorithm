import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
d = [0] * n
d[0] = m[0]
for i in range(n):
    d[i] = max(m[i], m[i] + d[i - 1])
print(max(d))
