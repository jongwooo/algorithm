import sys

n, m = map(int, sys.stdin.readline().split())
t = n
while n:
    n = n // m
    t += n
print(t)
