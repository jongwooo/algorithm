import sys


def move():
    global a
    moved = []
    for x, y in clouds:
        nx = (x + dir8[d - 1][0] * s) % n
        ny = (y + dir8[d - 1][1] * s) % n
        a[nx][ny] += 1
        moved.append((nx, ny))
    return moved


def water_copy_bug(moved):
    global a
    for x, y in moved:
        cnt = 0
        for dx, dy in dir4:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > 0:
                cnt += 1
        a[x][y] += cnt


def new_clouds():
    global a
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if (i, j) in moved_clouds or a[i][j] < 2:
                continue
            a[i][j] -= 2
            new_clouds.append((i, j))
    return new_clouds


n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
moves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
dir8 = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
dir4 = ((-1, -1), (-1, 1), (1, -1), (1, 1))
clouds = ((n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1))
for d, s in moves:
    moved_clouds = move()
    water_copy_bug(moved_clouds)
    clouds = new_clouds()
result = 0
for b in a:
    result += sum(b)
print(result)
