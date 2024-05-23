import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_time = int(1e9)
height = 0
for floor in range(256 + 1):
    exceed_block, lack_block = 0, 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] > floor:
                exceed_block += ground[i][j] - floor
            else:
                lack_block += floor - ground[i][j]
    if exceed_block + b >= lack_block and (exceed_block * 2) + lack_block <= min_time:
        min_time = (exceed_block * 2) + lack_block
        height = floor
print(min_time, height)
