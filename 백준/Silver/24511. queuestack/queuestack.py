import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
queue = deque()
for i in range(n):
    if a[i] == 0:
        queue.appendleft(b[i])
for i in range(m):
    queue.append(c[i])
    print(queue.popleft(), end=' ')
