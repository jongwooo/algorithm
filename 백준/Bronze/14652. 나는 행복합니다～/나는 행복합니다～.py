import sys

n, m, k = map(int, sys.stdin.readline().split())
print(k // m, k % m)
