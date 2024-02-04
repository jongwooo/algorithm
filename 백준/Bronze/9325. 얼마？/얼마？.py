import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().split())
        s += q * p
    print(s)
