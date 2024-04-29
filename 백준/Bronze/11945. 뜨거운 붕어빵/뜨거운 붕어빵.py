import sys

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    print(sys.stdin.readline().rstrip()[::-1])
