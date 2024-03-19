import sys
from collections import deque


def bfs():
    while queue:
        x, y, case = queue.popleft()
        if case == 'J' and (x == 0 or y == 0 or x == r - 1 or y == c - 1) and maze[x][y] != '#':
            return maze[x][y] + 1
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if maze[nx][ny] != '#' and case == 'F':
                    queue.append((nx, ny, case))
                    maze[nx][ny] = '#'
                elif maze[x][y] != '#' and maze[nx][ny] == '.' and case == 'J':
                    queue.append((nx, ny, case))
                    maze[nx][ny] = maze[x][y] + 1
    return 'IMPOSSIBLE'


r, c = map(int, sys.stdin.readline().split())
pos_j = []
pos_f = []
maze = []
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
for i in range(r):
    temp = list(sys.stdin.readline().rstrip())
    for j in range(c):
        if temp[j] == 'J':
            pos_j.append((i, j))
        elif temp[j] == 'F':
            pos_f.append((i, j))
    maze.append(temp)
queue = deque([])
queue.append((pos_j[0][0], pos_j[0][1], 'J'))
maze[pos_j[0][0]][pos_j[0][1]] = 0
for fr, fc in pos_f:
    queue.append((fr, fc, 'F'))
    maze[fr][fc] = '#'
print(bfs())
