import sys


def initialize():
    global beads
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    dd = 0
    dist = 1
    move = 0
    idx = 0
    x, y = n // 2, n // 2
    while True:
        for _ in range(dist):
            idx2pos[idx] = (x, y)
            pos2idx[(x, y)] = idx
            beads[idx] = grid[x][y]
            nx = x + dx[dd]
            ny = y + dy[dd]
            if (nx, ny) == (0, -1):
                return
            idx += 1
            x, y = nx, ny
        dd = (dd + 1) % 4
        move += 1
        if move == 2:
            dist += 1
            move = 0


def blizzard(d, s):
    destroy(d, s)
    cleanup()
    while True:
        if not explode():
            break
        cleanup()
    change()


def destroy(d, s):
    global beads
    dx = (0, -1, 1, 0, 0)
    dy = (0, 0, 0, -1, 1)
    x, y = n // 2, n // 2
    for i in range(1, s + 1):
        nx = x + dx[d] * i
        ny = y + dy[d] * i
        beads[pos2idx[(nx, ny)]] = DESTROYED


def cleanup():
    global beads
    destroyed_cnt = beads.count(DESTROYED)
    beads = [bead for bead in beads if bead != DESTROYED] + [EMPTY] * destroyed_cnt


def explode():
    global beads, score
    flag = False
    cnt = 0
    target = 0
    for i in range(n ** 2):
        if beads[i] == beads[target]:
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                score += beads[target] * cnt
                for j in range(target, i):
                    beads[j] = DESTROYED
            cnt = 1
            target = i
    return flag


def change():
    global beads
    new_beads = [EMPTY]
    group = []
    for i in range(1, n ** 2, 1):
        if not group or beads[i] == group[0]:
            group.append(beads[i])
        else:
            new_beads.append(len(group))
            new_beads.append(group[0])
            group = [beads[i]]
    beads = [EMPTY] * (n ** 2)
    for i in range(len(new_beads)):
        if i >= (n ** 2):
            break
        beads[i] = new_beads[i]


EMPTY = 0
DESTROYED = -1
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
beads = [-1] * (n ** 2)
idx2pos = {}
pos2idx = {}
initialize()
score = 0
for _ in range(m):
    d, s = map(int, sys.stdin.readline().split())
    blizzard(d, s)
print(score)
