import sys


def initialize():
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    x = N // 2
    y = N // 2
    idx = 0
    dist = 1
    direction = 0
    move = 0
    while True:
        for _ in range(dist):
            beads[idx] = grid[x][y]
            n2loc[idx] = (x, y)
            loc2n[(x, y)] = idx
            nx = x + dx[direction]
            ny = y + dy[direction]
            if (nx, ny) == (0, -1):
                return
            idx += 1
            x, y = nx, ny
        move += 1
        direction = (direction + 1) % 4
        if move == 2:
            dist += 1
            move = 0


def blizzard(d, s):
    destroy(d, s)
    tidy_up()
    while True:
        if not explode():
            break
        tidy_up()
    change()


def destroy(d, s):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    x = N // 2
    y = N // 2
    for i in range(1, s + 1):
        nx = x + dx[d - 1] * i
        ny = y + dy[d - 1] * i
        beads[loc2n[(nx, ny)]] = -1


def explode():
    global result
    flag = False
    cnt = 0
    target = 0
    for i in range(N ** 2):
        if beads[i] == beads[target]:
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                result += beads[target] * cnt
                for n in range(target, i):
                    beads[n] = -1
            cnt = 1
            target = i
    return flag


def tidy_up():
    global beads
    destroyed_cnt = beads.count(-1)
    beads = [bead for bead in beads if bead != -1] + [0] * destroyed_cnt


def change():
    global beads
    new_beads = [0]
    group = []
    for n in range(1, N ** 2, 1):
        if not group:
            group.append(beads[n])
        elif beads[n] == group[0]:
            group.append(beads[n])
        else:
            new_beads.append(len(group))
            new_beads.append(group[0])
            group = [beads[n]]
    beads = [0] * (N ** 2)
    for i in range(len(new_beads)):
        if i >= (N ** 2):
            break
        beads[i] = new_beads[i]


N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
beads = [-1] * (N ** 2)
n2loc = {}
loc2n = {}
initialize()
magics = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
result = 0
for d, s in magics:
    blizzard(d, s)
print(result)
