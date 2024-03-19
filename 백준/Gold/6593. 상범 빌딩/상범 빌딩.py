import sys
from collections import deque


def bfs():
    while queue:
        h, x, y = queue.popleft()
        if (h, x, y) == end:
            return f'Escaped in {building[h][x][y]} minute(s).'
        for dh, dx, dy in dirs:
            nh = h + dh
            nx = x + dx
            ny = y + dy
            if (0 <= nh < L and 0 <= nx < R and 0 <= ny < C and
                    (building[nh][nx][ny] == '.' or building[nh][nx][ny] == 'E')):
                queue.append((nh, nx, ny))
                building[nh][nx][ny] = building[h][x][y] + 1
    return 'Trapped!'


dirs = ((0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0))
while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == R == C == 0:
        break
    building = []
    start = tuple()
    end = tuple()
    for i in range(L):
        floor = []
        for j in range(R):
            temp = list(sys.stdin.readline().rstrip())
            for k in range(C):
                if temp[k] == 'S':
                    start = (i, j, k)
                elif temp[k] == 'E':
                    end = (i, j, k)
            floor.append(temp)
        building.append(floor)
        _ = sys.stdin.readline().rstrip()
    queue = deque([])
    queue.append(start)
    building[start[0]][start[1]][start[2]] = 0
    print(bfs())
