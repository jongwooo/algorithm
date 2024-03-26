import sys
from collections import deque


def find_fishes():
    fishes = []
    queue = deque([(shark_x, shark_y)])
    distance = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[shark_x][shark_y] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] <= shark_size:
                queue.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                if 0 < graph[nx][ny] < shark_size:
                    fishes.append((distance[nx][ny], nx, ny))
    return sorted(fishes)


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark_x, shark_y, shark_size = 0, 0, 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
cnt = 0
time = 0
while True:
    eat_candidates = find_fishes()
    if not eat_candidates:
        break
    dist, next_x, next_y = eat_candidates.pop(0)
    time += dist
    graph[shark_x][shark_y] = 0
    graph[next_x][next_y] = 9
    shark_x, shark_y = next_x, next_y
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
print(time)
