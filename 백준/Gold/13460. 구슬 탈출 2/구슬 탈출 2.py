import sys
from collections import deque


def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by)])
    visited = [(rx, ry, bx, by)]
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            rx, ry, bx, by = queue.popleft()
            if cnt > 10:
                return -1
            if board[rx][ry] == 'O':
                return cnt
            for dx, dy in dirs:
                nrx, nry = rx, ry
                while True:
                    nrx += dx
                    nry += dy
                    if board[nrx][nry] == '#':
                        nrx -= dx
                        nry -= dy
                        break
                    if board[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True:
                    nbx += dx
                    nby += dy
                    if board[nbx][nby] == '#':
                        nbx -= dx
                        nby -= dy
                        break
                    if board[nbx][nby] == 'O':
                        break
                if board[nbx][nby] == 'O':
                    continue
                if (nrx, nry) == (nbx, nby):
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if (nrx, nry, nbx, nby) not in visited:
                    queue.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    return -1


N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
print(bfs(rx, ry, bx, by))
