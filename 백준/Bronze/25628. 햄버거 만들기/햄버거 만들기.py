import sys

a, b = map(int, sys.stdin.readline().split())
print(min(a // 2, b))
