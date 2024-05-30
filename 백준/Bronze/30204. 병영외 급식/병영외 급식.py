import sys

n, x = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
print(1 if sum(p) % x == 0 else 0)
