import heapq


def bfs():
    global result
    queue = []
    heapq.heappush(queue, (0, 0, 0))  # (time, x, y)
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    while queue:
        time, x, y = heapq.heappop(queue)
        if (x, y) == (n - 1, n - 1):
            if result > time:
                result = time
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                heapq.heappush(queue, (time + grid[nx][ny], nx, ny))
                visited[nx][ny] = 1


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    result = int(1e9)
    bfs()
    print(f'#{tc} {result}')
