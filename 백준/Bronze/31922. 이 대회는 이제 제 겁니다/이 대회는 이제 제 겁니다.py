import sys

a, p, c = map(int, sys.stdin.readline().split())
print(max(a + c, p))
