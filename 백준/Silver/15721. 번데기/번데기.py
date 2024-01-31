import sys

a = int(sys.stdin.readline())
t = int(sys.stdin.readline())
s = int(sys.stdin.readline())
n = 2
cur = 0
while t != 0:
    for j in range(4):
        if j % 2 == 0:
            if s == 0:
                t -= 1
        else:
            if s == 1:
                t -= 1
        if t == 0:
            print(cur)
            exit(0)
        cur += 1
        if cur == a:
            cur = 0
    for j in range(n):
        if s == 0:
            t -= 1
        if t == 0:
            print(cur)
            exit(0)
        cur += 1
        if cur == a:
            cur = 0
    for j in range(n):
        if s == 1:
            t -= 1
        if t == 0:
            print(cur)
            exit(0)
        cur += 1
        if cur == a:
            cur = 0
    n += 1
