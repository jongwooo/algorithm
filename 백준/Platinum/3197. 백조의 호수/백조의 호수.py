import sys
from collections import deque


def find(v):
    if v == root[v[0]][v[1]]:
        return v
    root[v[0]][v[1]] = find(root[v[0]][v[1]])
    return root[v[0]][v[1]]


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)
    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
        root[r2[0]][r2[1]] = r1
    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
        root[r1[0]][r1[1]] = r2
    else:
        root[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1


dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
r, c = map(int, sys.stdin.readline().split())
lake = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
root = [[(i, j) for j in range(c)] for i in range(r)]
rank = [[0] * c for i in range(r)]
visited = [[False] * c for _ in range(r)]
swan = []
for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            swan.append((i, j))
            lake[i][j] = '.'
            if len(swan) == 2:
                break
melt = deque()
for i in range(r):
    for j in range(c):
        if not visited[i][j] and lake[i][j] == '.':
            queue = deque([(i, j)])
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()
                root[x][y] = (i, j)
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if not visited[nx][ny] and lake[nx][ny] == '.':
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                        elif not visited[nx][ny] and lake[nx][ny] == 'X':
                            visited[nx][ny] = True
                            melt.append((nx, ny))
day = 0
while find(swan[0]) != find(swan[1]):
    temp = deque()
    while melt:
        x, y = melt.popleft()
        lake[x][y] = '.'
        merge_point = []
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and lake[nx][ny] == 'X':
                    visited[nx][ny] = 1
                    temp.append((nx, ny))
                elif lake[nx][ny] == '.':
                    merge_point.append((nx, ny))
        for rt in merge_point:
            if find(rt) != find((x, y)):
                union(rt, (x, y))
    melt = temp
    day += 1
print(day)
