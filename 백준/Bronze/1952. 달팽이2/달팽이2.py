import sys

m, n = map(int, sys.stdin.readline().split())
print(n * 2 - 1 if m > n else m * 2 - 2)
