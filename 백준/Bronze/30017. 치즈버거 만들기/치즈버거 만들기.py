import sys

a, b = map(int, sys.stdin.readline().split())
print(3 + 2 * min(a - 2, b - 1))
