import copy
import sys


def int_minus_one():
    return lambda x: int(x) - 1


def in_range(a, b):
    return 0 <= a < 4 and 0 <= b < 4


def clone_spell():
    global clone
    clone = copy.deepcopy(fishes)


def fishes_move():
    global fishes
    moved = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            if fishes[x][y]:
                while fishes[x][y]:
                    fd = fishes[x][y].pop()
                    for _ in range(8):
                        dx, dy = fish_dirs[fd]
                        nx = x + dx
                        ny = y + dy
                        if in_range(nx, ny) and (nx, ny) != (sx, sy) and not smells[nx][ny]:
                            moved[nx][ny].append(fd)
                            break
                        fd = (fd - 1) % 8
                    else:
                        moved[x][y].append(fd)
    fishes = moved


def shark_move():
    global fishes, max_eat_cnt
    max_eat_cnt = -1
    dfs(sx, sy, 0, 0, [])
    for x, y in eaten:
        if fishes[x][y]:
            fishes[x][y] = []
            smells[x][y] = 3


def dfs(x, y, depth, eat_cnt, visited):
    global sx, sy, eaten, max_eat_cnt
    if depth == 3:
        if max_eat_cnt < eat_cnt:
            max_eat_cnt = eat_cnt
            sx, sy = x, y
            eaten = visited[:]
        return
    for dx, dy in shark_dirs:
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny):
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                dfs(nx, ny, depth + 1, eat_cnt + len(fishes[nx][ny]), visited)
                visited.pop()
            else:
                dfs(nx, ny, depth + 1, eat_cnt, visited)


def remove_smells():
    global smells
    for i in range(4):
        for j in range(4):
            if smells[i][j]:
                smells[i][j] -= 1


def append_clone_spell():
    global fishes
    for i in range(4):
        for j in range(4):
            fishes[i][j] += clone[i][j]


fish_dirs = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
shark_dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))
m, s = map(int, sys.stdin.readline().split())
fishes = [[[] for _ in range(4)] for _ in range(4)]
clone = []
eaten = []
max_eat_cnt = -1
for _ in range(m):
    fx, fy, d = map(int_minus_one(), sys.stdin.readline().split())
    fishes[fx][fy].append(d)
smells = [[0] * 4 for _ in range(4)]
sx, sy = map(int_minus_one(), sys.stdin.readline().split())
for _ in range(s):
    clone_spell()
    fishes_move()
    shark_move()
    remove_smells()
    append_clone_spell()
alive = 0
for i in range(4):
    for j in range(4):
        if fishes[i][j]:
            alive += len(fishes[i][j])
print(alive)
