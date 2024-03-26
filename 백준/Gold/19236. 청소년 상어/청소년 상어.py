import copy
import sys


def find_fish(fishes, fish):
    for i in range(4):
        for j in range(4):
            if fishes[i][j][0] == fish:
                return (i, j)


def fish_move(sx, sy, fishes):
    for fish in range(1, 17):
        position = find_fish(fishes, fish)
        if position:
            fx, fy = position[0], position[1]
            fd = fishes[fx][fy][1]
            for i in range(8):
                nd = (fd + i) % 8
                nx = fx + dir_x[nd]
                ny = fy + dir_y[nd]
                if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy):
                    fishes[fx][fy][1] = nd
                    fishes[nx][ny], fishes[fx][fy] = fishes[fx][fy], fishes[nx][ny]
                    break


def get_movable_position(sx, sy, fishes):
    sd = fishes[sx][sy][1]
    position = []
    for i in range(3):
        sx += dir_x[sd]
        sy += dir_y[sd]
        if 0 <= sx < 4 and 0 <= sy < 4 and fishes[sx][sy][0] > 0:
            position.append((sx, sy))
    return position


def dfs(sx, sy, score, fishes):
    global max_score
    fishes = copy.deepcopy(fishes)
    score += fishes[sx][sy][0]
    fishes[sx][sy][0] = 0
    fish_move(sx, sy, fishes)
    position = get_movable_position(sx, sy, fishes)
    if position:
        for nx, ny in position:
            dfs(nx, ny, score, fishes)
    else:
        max_score = max(max_score, score)


dir_x = (-1, -1, 0, 1, 1, 1, 0, -1)
dir_y = (0, -1, -1, -1, 0, 1, 1, 1)
fishes = [[] for _ in range(4)]
for i in range(4):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        fishes[i].append([temp[2 * j], temp[2 * j + 1] - 1])
max_score = 0
dfs(0, 0, 0, fishes)
print(max_score)
