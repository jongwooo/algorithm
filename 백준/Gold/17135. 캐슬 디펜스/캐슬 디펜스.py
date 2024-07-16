import sys
from collections import deque
from copy import deepcopy
from itertools import combinations


def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def archers_attack(pos):
    global copied_grid
    kill = 0
    candidates = []
    for ay in pos:
        ex, ey = find_enemy(n, ay)
        if (ex, ey) == (-1, -1):  # d 거리 이내에 적 없음
            continue
        candidates.append((ex, ey))  # 여러 궁수가 한 명의 적을 공격할 수 있다.
    for ex, ey in candidates:
        if copied_grid[ex][ey] == 1:
            copied_grid[ex][ey] = 0  # 적 제거
            kill += 1
    return kill


def find_enemy(ax, ay):
    if copied_grid[ax - 1][ay] == 1:
        return ax - 1, ay
    candidates = []  # 거리가 d 이하인 모든 적
    visited = [[0] * m for _ in range(n)]
    queue = deque([(ax - 1, ay)])
    visited[ax - 1][ay] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            dist = distance(ax, ay, nx, ny)
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and dist <= d:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                if copied_grid[nx][ny] == 1:
                    candidates.append((-dist, nx, ny))
    if not candidates:
        return -1, -1
    candidates.sort(key=lambda k: (-k[0], k[2]))
    return candidates[0][1:]


def enemies_move():
    global copied_grid
    temp = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if x < n - 1 and copied_grid[x][y] == 1:
                temp[x + 1][y] = 1
    copied_grid = temp


def game_over():
    for x in range(n):
        for y in range(m):
            if copied_grid[x][y] == 1:
                return False
    return True


dirs = ((-1, 0), (0, -1), (0, 1))  # 상, 좌, 우
n, m, d = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_cnt = 0
for archer_pos in list(combinations(range(m), 3)):  # 궁수 위치 경우의 수
    copied_grid = deepcopy(grid)
    cnt = 0
    while True:
        cnt += archers_attack(archer_pos)
        enemies_move()
        if game_over():
            break
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)
