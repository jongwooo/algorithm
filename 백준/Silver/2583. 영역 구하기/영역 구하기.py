import sys
from collections import deque


def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    table[y][x] = -1
    area = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and table[ny][nx] == 0:
                queue.append((ny, nx))
                table[ny][nx] = -1
                area += 1
    return area


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
m, n, k = map(int, sys.stdin.readline().split())
table = [[0] * n for _ in range(m)]
for _ in range(k):
    from_x, from_y, to_x, to_y = map(int, sys.stdin.readline().split())
    for y in range(from_y, to_y):
        for x in range(from_x, to_x):
            table[y][x] = 1
areas = []
for y in range(m):
    for x in range(n):
        if table[y][x] == 0:
            areas.append(bfs(y, x))
areas.sort()
print(len(areas))
print(*areas)
