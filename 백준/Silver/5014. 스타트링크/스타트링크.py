import sys
from collections import deque


def bfs(s):
    queue = deque([])
    queue.append(s)
    floor[s] = 1
    while queue:
        s = queue.popleft()
        if s == g:
            return floor[s] - 1
        for button in buttons:
            next_s = button(s)
            if 0 < next_s <= f and floor[next_s] == 0:
                queue.append(next_s)
                floor[next_s] = floor[s] + 1
    return 'use the stairs'


f, s, g, u, d = map(int, sys.stdin.readline().split())
floor = [0] * (f + 1)
buttons = (
    lambda x: x + u,
    lambda x: x - d
)
print(bfs(s))
