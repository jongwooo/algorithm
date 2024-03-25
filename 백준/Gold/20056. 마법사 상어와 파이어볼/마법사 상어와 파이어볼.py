import sys


def move():
    while fireballs:
        r, c, m, s, d = fireballs.pop()
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        board[nr][nc].append((m, s, d))


def merge_and_split():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:
                nm, ns = 0, 0
                odd_cnt, even_cnt = 0, 0
                cnt = 0
                while board[i][j]:
                    m, s, d = board[i][j].pop()
                    nm += m
                    ns += s
                    if d % 2:
                        odd_cnt += 1
                    else:
                        even_cnt += 1
                    cnt += 1
                if odd_cnt == cnt or even_cnt == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if nm // 5:
                    for dd in nd:
                        fireballs.append((i, j, nm // 5, ns // cnt, dd))
            elif len(board[i][j]) == 1:
                m, s, d = board[i][j].pop()
                fireballs.append((i, j, m, s, d))


N, M, K = map(int, sys.stdin.readline().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))
board = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)
for _ in range(K):
    move()
    merge_and_split()
sum_m = 0
for _, _, m, _, _ in fireballs:
    sum_m += m
print(sum_m)
