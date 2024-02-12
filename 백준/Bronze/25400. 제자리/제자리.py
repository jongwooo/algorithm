import sys
from collections import deque

n = int(sys.stdin.readline())
a = deque(list(map(int, sys.stdin.readline().split())))
cur = 1
cnt = 0
while a:
    x = a.popleft()
    if x == cur:
        cur += 1
    else:
        cnt += 1
print(cnt)
