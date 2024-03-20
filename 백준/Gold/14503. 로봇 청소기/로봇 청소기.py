import sys
from collections import deque


def bfs():
    global d
    cnt = 1
    queue = deque([])
    queue.append((r, c))
    while queue:
        x, y = queue.popleft()
        clean = False
        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
                clean = True
                break
        if not clean:
            if room[x - dx[d]][y - dy[d]] == 1:
                print(cnt)
                break
            else:
                queue.append((x - dx[d], y - dy[d]))


n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[r][c] = True
bfs()
