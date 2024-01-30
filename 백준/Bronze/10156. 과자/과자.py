import sys

k, n, m = map(int, sys.stdin.readline().split())
print(0 if k * n < m else k * n - m)
