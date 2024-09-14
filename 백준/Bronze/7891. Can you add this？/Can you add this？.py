import sys

t = int(sys.stdin.readline())
for _ in range(t):
    print(sum(map(int, sys.stdin.readline().split())))
