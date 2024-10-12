import sys

a, b = map(int, sys.stdin.readline().split())
m = (b - a) / 400
print(1 / (1 + 10 ** m))
