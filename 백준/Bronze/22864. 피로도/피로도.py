import sys

a, b, c, m = map(int, sys.stdin.readline().split())
if a > m:
    print(0)
else:
    f = 0
    work = 0
    hour = 0
    while hour < 24:
        hour += 1
        if f + a <= m:
            f += a
            work += b
        else:
            if f < c:
                f = 0
            else:
                f -= c
    print(work)
