import sys
from collections import deque


def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        if y == to_y and x == to_x:
            break
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < length and 0 <= nx < length and not visited[ny][nx]:
                queue.append((ny, nx))
                board[ny][nx] = board[y][x] + 1
                visited[ny][nx] = True


t = int(sys.stdin.readline())
dy = [2, 2, 1, 1, -1, -1, -2, -2]
dx = [-1, 1, -2, 2, -2, 2, -1, 1]
for _ in range(t):
    length = int(sys.stdin.readline())
    from_x, from_y = map(int, sys.stdin.readline().split())
    to_x, to_y = map(int, sys.stdin.readline().split())
    board = [[0] * length for _ in range(length)]
    visited = [[False] * length for _ in range(length)]
    bfs(from_y, from_x)
    print(board[to_y][to_x])
