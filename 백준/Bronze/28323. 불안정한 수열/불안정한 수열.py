import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
queue = deque(a)
cnt = 0
while queue:
    x = queue.popleft()
    if len(queue) > 0:
        if (x + queue[0]) % 2 != 0:
            cnt += 1
        else:
            queue.popleft()
            queue.appendleft(x)
print(cnt + 1)
