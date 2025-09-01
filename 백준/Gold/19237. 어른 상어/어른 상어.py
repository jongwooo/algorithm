import sys


def minus_one():
    return lambda x: int(x) - 1


def update_smell():
    global smells
    for i in range(n):
        for j in range(n):
            if smells[i][j][0] > 0 and smells[i][j][1] <= time:  # 상어가 k번 이동하고 나면
                smells[i][j] = [0, 0]  # 냄새는 사라진다.
            if grid[i][j] != 0:
                smells[i][j] = [grid[i][j], time + k]  # (상어 번호, 냄새 유효 기간)


def shark_move():  # 각 상어가 움직인다.
    global directions, grid
    temp = [[0] * n for _ in range(n)]
    # 각 상어를 순회하며 이동시킨다.
    for x in range(n):
        for y in range(n):
            if grid[x][y] != 0:
                sid = grid[x][y]
                direction = directions[sid - 1]
                found_blank_space = False
                for d in priorities[sid - 1][direction]:  # 현재 방향에 따른 우선순위
                    nx = x + dir_x[d]
                    ny = y + dir_y[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smells[nx][ny][0] == 0:
                            directions[sid - 1] = d
                            if temp[nx][ny] == 0:
                                temp[nx][ny] = sid
                            else:
                                temp[nx][ny] = min(sid, temp[nx][ny])  # 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫒겨난다.
                            found_blank_space = True
                            break
                if not found_blank_space:  # 주변에 모두 냄새가 남아 있다면, 자신의 냄새 방향으로 이동한다.
                    for d in priorities[sid - 1][direction]:
                        nx = x + dir_x[d]
                        ny = y + dir_y[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if smells[nx][ny][0] == sid:
                                directions[sid - 1] = d
                                temp[nx][ny] = sid
                                break
    grid = temp


def only_1st_shark_remain_in_grid():  # 1번 상어만 격자에 남아 있는지 확인한다.
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 1:
                return False
    return True


dir_x = (-1, 1, 0, 0)
dir_y = (0, 0, -1, 1)
n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
smells = [[[0, 0] for _ in range(n)] for _ in range(n)]
time = 0  # 현재 시간
directions = list(map(minus_one(), sys.stdin.readline().split()))  # 각 상어의 방향 (위, 아래, 왼쪽, 오른쪽)
priorities = [[list(map(minus_one(), sys.stdin.readline().split())) for _ in range(4)] for _ in range(m)]
while True:
    update_smell()
    shark_move()
    time += 1
    if only_1st_shark_remain_in_grid():  # 1번 상어만 격자에 남은 경우
        break
    if time >= 1_000:  # 1,000초가 넘어도 다른 상어가 격자에 남아 있으면
        time = -1  # -1을 출력한다.
        break
print(time)
