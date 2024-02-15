import sys
from collections import deque


def bfs(y, x, h, visited):
    queue = deque([])
    queue.append((y, x))
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if area[ny][nx] > h:
                    queue.append((ny, nx))
                    visited[ny][nx] = True


n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_height = max(map(max, area))
min_height = min(map(min, area))
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
max_cnt = 0
for h in range(min_height - 1, max_height):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if area[y][x] > h and not visited[y][x]:
                bfs(y, x, h, visited)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
