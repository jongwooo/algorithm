import sys

a, b = map(int, sys.stdin.readline().split())
print(0 if a - (b / 100 * a) >= 100.0 else 1)
