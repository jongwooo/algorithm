import sys
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        fire = False
        if visited[x][y] == '*':
            fire = True
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if (building[nx][ny] == '.' or building[nx][ny] == '@') and visited[nx][ny] == -1:
                    if fire:
                        visited[nx][ny] = '*'
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
            else:
                if not fire:
                    return visited[x][y] + 1
    return 'IMPOSSIBLE'


dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    building = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]
    queue = deque([])
    start = tuple()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                visited[i][j] = 0
                start = (i, j)
            elif building[i][j] == '*':
                visited[i][j] = '*'
                queue.append((i, j))
    queue.append(start)
    print(bfs())
