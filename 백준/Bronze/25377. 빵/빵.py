import sys

n = int(sys.stdin.readline())
min_time = 1001
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        continue
    min_time = min(min_time, b)
print(-1 if min_time == 1001 else min_time)
