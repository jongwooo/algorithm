import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
cnt = 0
for ai in a:
    ai -= b
    cnt += 1
    if ai > 0:
        cnt += (ai // c)
        if ai % c > 0:
            cnt += 1
print(cnt)
