from collections import deque


def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True
                result[ny][nx] = result[y][x] + 1


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = deque([])
for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            queue.append((y, x))
            result[y][x] = 0
            visited[y][x] = True
        if board[y][x] == 0:
            result[y][x] = 0
bfs()
for r in result:
    print(*r)
