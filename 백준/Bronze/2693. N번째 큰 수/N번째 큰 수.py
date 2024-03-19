import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a = sorted(list(map(int, sys.stdin.readline().split())))
    print(a[-3])
