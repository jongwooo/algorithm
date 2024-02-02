import sys

t = int(sys.stdin.readline())
for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    print(e - v + 2)
