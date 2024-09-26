import sys

n, m, k = map(int, sys.stdin.readline().split())
print(min(m, k) + n - max(m, k))
