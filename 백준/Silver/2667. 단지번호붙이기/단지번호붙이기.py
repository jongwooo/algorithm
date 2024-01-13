from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    graph[y][x] = 0
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = 0
                cnt += 1
    return cnt


result = []
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            result.append(bfs(y, x))
print(len(result))
for i in sorted(result):
    print(i)
