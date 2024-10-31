import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def bfs():
    visited = [[1] * 5 for _ in range(5)]
    for x, y in pos:
        visited[x][y] = 0
    queue = deque([pos[0]])
    visited[pos[0][0]][pos[0][1]] = 1
    check = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                check += 1
    return check == 7


def dfs(depth, start, y_cnt):
    global formed_cnt
    if y_cnt >= 4:
        return
    if depth == 7:
        if bfs():
            formed_cnt += 1
        return
    for i in range(start, 25):
        x = i // 5
        y = i % 5
        pos.append((x, y))
        dfs(depth + 1, i + 1, y_cnt + (matrix[x][y] == 'Y'))
        pos.pop()


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
pos = []
formed_cnt = 0
dfs(0, 0, 0)
print(formed_cnt)
