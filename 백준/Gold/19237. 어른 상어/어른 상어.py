def int_minus_one():
    return lambda x: int(x) - 1


def in_range(a, b):
    return 0 <= a < n and 0 <= b < n


def update_smell():
    global smell
    for i in range(n):
        for j in range(n):
            if smell[i][j][0] and smell[i][j][1] <= time:
                smell[i][j] = (0, 0)
            if grid[i][j] != EMPTY:
                smell[i][j] = (grid[i][j], time + k)


def sharks_move():
    global shark_d, grid
    temp = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y] != EMPTY:
                sid = grid[x][y]
                sd = shark_d[sid - 1]
                found_empty_space = 0
                for d in shark_priority_d[sid - 1][sd]:
                    nx = x + dir_x[d]
                    ny = y + dir_y[d]
                    if in_range(nx, ny) and smell[nx][ny][0] == 0:
                        shark_d[sid - 1] = d
                        if temp[nx][ny] == EMPTY:
                            temp[nx][ny] = sid
                        else:
                            temp[nx][ny] = min(temp[nx][ny], sid)
                        found_empty_space = 1
                        break
                if not found_empty_space:
                    for d in shark_priority_d[sid - 1][sd]:
                        nx = x + dir_x[d]
                        ny = y + dir_y[d]
                        if in_range(nx, ny) and smell[nx][ny][0] == sid:
                            shark_d[sid - 1] = d
                            temp[nx][ny] = sid
                            break
    grid = temp


def only_1st_shark_remain():
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 1:
                return False
    return True


EMPTY = 0
dir_x = (-1, 1, 0, 0)
dir_y = (0, 0, -1, 1)
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
smell = [[(0, 0) for _ in range(n)] for _ in range(n)]
shark_d = list(map(int_minus_one(), input().split()))
shark_priority_d = [[list(map(int_minus_one(), input().split())) for _ in range(4)] for _ in range(m)]
time = 0
while True:
    update_smell()
    sharks_move()
    time += 1
    if only_1st_shark_remain():
        break
    if time >= 1_000:
        time = -1
        break
print(time)
