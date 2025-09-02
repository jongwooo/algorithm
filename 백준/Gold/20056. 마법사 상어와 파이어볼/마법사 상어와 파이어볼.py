import sys
from collections import deque


def fireballs_move():
    while fireballs:
        r, c, m, s, d = fireballs.popleft()
        nr = (r + dr[d] * s) % n
        nc = (c + dc[d] * s) % n
        grid[nr][nc].append((m, s, d))


def merge_and_split():
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) >= 2:
                nm, ns = 0, 0
                odd_cnt, even_cnt = 0, 0
                cnt = 0
                while grid[i][j]:
                    m, s, d = grid[i][j].pop()
                    nm += m
                    ns += s
                    if d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                    cnt += 1
                if odd_cnt == cnt or even_cnt == cnt:
                    nd = (0, 2, 4, 6)
                else:
                    nd = (1, 3, 5, 7)
                if nm // 5:
                    for dd in nd:
                        fireballs.append((i, j, nm // 5, ns // cnt, dd))
            elif len(grid[i][j]) == 1:
                m, s, d = grid[i][j].pop()
                fireballs.append((i, j, m, s, d))




dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)
n, m, k = map(int, sys.stdin.readline().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
fireballs = deque([])
for i in range(1, m + 1):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs.append((r - 1, c - 1, m, s, d))
for _ in range(k):
    fireballs_move()
    merge_and_split()
m_sum = 0
for _, _, m, _, _ in fireballs:
    m_sum += m
print(m_sum)
