import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    while queue:
        max_priority = max(queue)
        first = queue.popleft()
        m -= 1
        if max_priority == first:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(first)
            if m < 0:
                m = len(queue) - 1
