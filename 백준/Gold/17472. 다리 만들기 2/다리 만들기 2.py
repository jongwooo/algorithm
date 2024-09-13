import sys
from collections import deque


def bfs(x, y):
    global grid, visited
    queue = deque([(x, y)])
    grid[x][y] = island_num
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                grid[nx][ny] = island_num
                visited[nx][ny] = True


def find_edges(x, y, now):
    global edges
    queue = deque([])
    for d in range(4):
        queue.append((x, y, 0, d))
    while queue:
        x, y, dist, d = queue.popleft()
        if grid[x][y] != 0 and grid[x][y] != now:
            if dist > 2:
                edges.add((dist - 1, now, grid[x][y]))
            continue
        nx = x + dirs[d][0]
        ny = y + dirs[d][1]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != now:
            queue.append((nx, ny, dist + 1, d))


def find(k):
    global parent
    if k != parent[k]:
        parent[k] = find(parent[k])
    return parent[k]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
island_num = 1
for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            bfs(i, j)
            island_num += 1
edges = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0:
            find_edges(i, j, grid[i][j])
edges = list(edges)
edges.sort()
parent = [i for i in range(island_num)]
result = 0
num = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost
        num += 1
if result == 0 or num != island_num - 2:
    print(-1)
else:
    print(result)
