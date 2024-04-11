import copy
import sys


def clone_spell():
    global clone
    clone = copy.deepcopy(fishes)


def fishes_move():
    global fishes
    moved = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while fishes[x][y]:
                fd = fishes[x][y].pop()
                for _ in range(8):
                    dx, dy = fish_dirs[fd]
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny] and (nx, ny) != (sx, sy):
                        moved[nx][ny].append(fd)
                        break
                    fd = (fd - 1) % 8
                else:
                    moved[x][y].append(fd)
    fishes = moved


def shark_move():
    global fishes, eaten, max_eat
    max_eat = -1
    dfs(sx, sy, 0, 0, [])
    for x, y in eaten:
        if fishes[x][y]:
            fishes[x][y] = []
            smell[x][y] = 3


def dfs(x, y, depth, eat_cnt, visited):
    global sx, sy, eaten, max_eat
    if depth == 3:
        if max_eat < eat_cnt:
            max_eat = eat_cnt
            sx, sy = x, y
            eaten = visited[:]
        return
    for dx, dy in shark_dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                dfs(nx, ny, depth + 1, eat_cnt + len(fishes[nx][ny]), visited)
                visited.pop()
            else:
                dfs(nx, ny, depth + 1, eat_cnt, visited)


def remove_smell():
    for x in range(4):
        for y in range(4):
            if smell[x][y]:
                smell[x][y] -= 1


def append_clone_to_fishes():
    global fishes
    for x in range(4):
        for y in range(4):
            fishes[x][y] += clone[x][y]


m, s = map(int, sys.stdin.readline().split())
fishes = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]
clone = []
eaten = []
max_eat = -1
fish_dirs = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
shark_dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))
for _ in range(m):
    r, c, d = map(int, sys.stdin.readline().split())
    fishes[r - 1][c - 1].append(d - 1)
sx, sy = map(lambda x: int(x) - 1, sys.stdin.readline().split())
for _ in range(s):
    clone_spell()
    fishes_move()
    shark_move()
    remove_smell()
    append_clone_to_fishes()
alive = 0
for i in range(4):
    for j in range(4):
        alive += len(fishes[i][j])
print(alive)
