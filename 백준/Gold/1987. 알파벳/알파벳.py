import sys


def dfs(y, x, cnt):
    global max_route
    max_route = max(max_route, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in visited:
            visited.add(board[ny][nx])
            dfs(ny, nx, cnt + 1)
            visited.remove(board[ny][nx])


r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(r)]
visited = set(board[0][0])
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
max_route = 0
dfs(0, 0, 1)
print(max_route)
