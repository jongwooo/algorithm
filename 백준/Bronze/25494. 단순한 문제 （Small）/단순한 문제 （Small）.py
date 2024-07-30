import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    print(min(a, b, c))
