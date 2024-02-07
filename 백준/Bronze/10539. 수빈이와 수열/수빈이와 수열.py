import sys

n = int(sys.stdin.readline())
a = [0] * n
b = list(map(int, sys.stdin.readline().split()))
s = 0
for i in range(n):
    a[i] = b[i] * (i + 1) - s
    s += a[i]
print(*a)
