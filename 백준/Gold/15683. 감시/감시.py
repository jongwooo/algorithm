import copy
import sys


def dfs(office, cctv_id):
    global blind_spot_cnt
    if cctv_id == len(cctv_info):
        blind_spot_cnt = min(blind_spot_cnt, count_blind_spots(office))
        return
    x, y, cctv_type = cctv_info[cctv_id]
    for cctv_dir in cctv_range[cctv_type]:
        office_copy = copy.deepcopy(office)
        find_blind_spots(office_copy, x, y, cctv_dir)
        dfs(office_copy, cctv_id + 1)


def find_blind_spots(office, x, y, cctv_dir):
    for d in cctv_dir:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or N <= nx or ny < 0 or M <= ny or office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                office[nx][ny] = '#'


def count_blind_spots(office):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
office = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv_range = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}
cctv_info = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv_info.append((i, j, office[i][j]))
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
blind_spot_cnt = N * M
dfs(office, 0)
print(blind_spot_cnt)
