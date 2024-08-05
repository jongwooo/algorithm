import sys

p, n = map(int, sys.stdin.readline().split())
a = sorted(list(map(int, sys.stdin.readline().split())))
max_cnt = 0
for ai in a:
    if p < 200:
        p += ai
        max_cnt += 1
    else:
        break
print(max_cnt)
