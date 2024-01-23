from collections import deque


def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
for row in range(n):
    for col in range(m):
        if box[row][col] == 1:
            queue.append((row, col))
bfs()
min_day = 0
for b in box:
    for i in range(m):
        if b[i] == 0:
            print(-1)
            exit()
    min_day = max(min_day, max(b))
print(min_day - 1)
