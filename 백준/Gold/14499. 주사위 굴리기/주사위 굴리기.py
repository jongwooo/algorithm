import sys


def roll_dice(d):
    global dice, x, y
    dx, dy = dirs[d]
    nx = x + dx
    ny = y + dy
    if nx < 0 or n <= nx or ny < 0 or m <= ny:
        return
    x, y = nx, ny
    temp_dice = dice[:]
    if d == 0:  # 동
        dice = [temp_dice[left], temp_dice[right], temp_dice[top], temp_dice[bottom], temp_dice[down], temp_dice[up]]
    elif d == 1:  # 서
        dice = [temp_dice[right], temp_dice[left], temp_dice[bottom], temp_dice[top], temp_dice[down], temp_dice[up]]
    elif d == 2:  # 북
        dice = [temp_dice[down], temp_dice[up], temp_dice[right], temp_dice[left], temp_dice[bottom], temp_dice[top]]
    else:  # 남
        dice = [temp_dice[up], temp_dice[down], temp_dice[right], temp_dice[left], temp_dice[top], temp_dice[bottom]]
    if grid[x][y] == 0:
        grid[x][y] = dice[bottom]
    else:
        dice[bottom] = grid[x][y]
        grid[x][y] = 0
    print(dice[top])


n, m, x, y, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
top, bottom, right, left, down, up = 0, 1, 2, 3, 4, 5  # 위, 아래, 동서남북 순서
dice = [0] * 6
dirs = ((0, 1), (0, -1), (-1, 0), (1, 0))  # 동 서 북 남
commands = list(map(lambda i: int(i) - 1, sys.stdin.readline().split()))
for d in commands:
    roll_dice(d)
