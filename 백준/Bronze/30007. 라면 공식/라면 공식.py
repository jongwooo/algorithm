import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b, x = map(int, sys.stdin.readline().split())
    print(a * (x - 1) + b)
