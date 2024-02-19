import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
queue = deque([k for k in range(1, n + 1)])
cnt = 0
for i in a:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
