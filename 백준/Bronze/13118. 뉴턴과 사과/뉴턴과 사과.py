import sys

p = list(map(int, sys.stdin.readline().split()))
x, y, r = map(int, sys.stdin.readline().split())
print(p.index(x) + 1 if x in p else 0)
