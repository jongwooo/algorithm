import sys

n, m, k = map(int, sys.stdin.readline().split())
print(max(0, n - m * k), max(0, n - m * (k - 1) - 1))
