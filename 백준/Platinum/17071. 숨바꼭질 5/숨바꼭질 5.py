import sys
from collections import deque


def bfs():
    queue = deque([(n, 0)])
    visited[n][0] = 0
    while queue:
        now, second = queue.popleft()
        for next_node in (now - 1, now + 1, 2 * now):
            if 0 <= next_node < 500_001 and visited[next_node][(second + 1) % 2] == -1:
                queue.append((next_node, second + 1))
                visited[next_node][(second + 1) % 2] = second + 1
    return -1


n, k = map(int, sys.stdin.readline().split())
visited = [[-1] * 2 for _ in range(500_001)]
bfs()
result = -1
second = 0
for t in range(500_001):
    k += t
    if k > 500_000: 
        break
    if visited[k][second % 2] <= second:
        result = second
        break
    second += 1
print(result)
