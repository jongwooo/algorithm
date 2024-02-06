import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(sum(list(map(int, sys.stdin.readline().split()))))
