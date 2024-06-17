import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())
    cnt = 0
    for _ in range(n):
        v, f, c = map(int, sys.stdin.readline().split())
        if v * f / c >= d:
            cnt += 1
    print(cnt)
