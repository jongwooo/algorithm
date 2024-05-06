import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    t1, t2, t3 = map(int, sys.stdin.readline().split())
    if t1 == t2 == t3 == -1:
        continue
    if t1 == -1:
        t1 = 121
    if t2 == -1:
        t2 = 121
    if t3 == -1:
        t3 = 121
    if t1 <= t2 <= t3:
        cnt += 1
print(cnt)
