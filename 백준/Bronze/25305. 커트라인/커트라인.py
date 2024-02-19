import sys

n, k = map(int, sys.stdin.readline().split())
x = sorted(list(map(int, sys.stdin.readline().split())))
print(x[-k])
