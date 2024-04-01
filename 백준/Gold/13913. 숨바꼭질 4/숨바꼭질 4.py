import sys
from collections import deque


def bfs():
    queue = deque([n])
    while queue:
        now = queue.popleft()
        if now == k:
            print(visited[now])
            route = []
            temp = now
            for _ in range(visited[now] + 1):
                route.append(temp)
                temp = prev[temp]
            print(*route[::-1])
            return
        for next_node in (now - 1, now + 1, 2 * now):
            if 0 <= next_node < 100_001 and visited[next_node] == 0:
                queue.append(next_node)
                visited[next_node] = visited[now] + 1
                prev[next_node] = now


n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100_001
prev = [0] * 100_001
bfs()
