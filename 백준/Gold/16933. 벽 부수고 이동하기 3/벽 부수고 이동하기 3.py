import sys
from collections import deque


def bfs():
    global board, visited
    queue = deque([(0, 0, 0, 1)])
    visited[0][0][0] = 1
    while queue:
        x, y, cnt, dist = queue.popleft()
        if (x, y) == (n - 1, m - 1):  # (N, M) 위치
            return dist
        daytime = dist % 2
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and not visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = dist
                    queue.append((nx, ny, cnt, dist + 1))
                elif board[nx][ny] == 1 and cnt < k and not visited[nx][ny][cnt + 1]:
                    if daytime:
                        visited[nx][ny][cnt + 1] = dist
                        queue.append((nx, ny, cnt + 1, dist + 1))
                    else:
                        queue.append((x, y, cnt, dist + 1))
    return -1  # 불가능


n, m, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
print(bfs())
