import sys

a, b, c = sorted(map(int, sys.stdin.readline().split()))
print(a + b + min(c, a + b - 1))
