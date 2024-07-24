import sys


def dfs(x, y, depth, temp):
    global max_num, visited
    if depth == 4:
        if max_num < temp:
            max_num = temp
        return
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, temp + paper[nx][ny])
            visited[nx][ny] = 0


def t_block(x, y):
    global max_num, visited
    candidates = []
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            candidates.append(paper[nx][ny])
    length = len(candidates)
    if length < 3 or length > 4:
        return
    candidates.sort(reverse=True)
    if length == 4:
        candidates.pop()
    temp = paper[x][y] + sum(candidates)
    if max_num < temp:
        max_num = temp


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_num = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        t_block(i, j)
        visited[i][j] = 0
print(max_num)
