import sys

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
grid = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
total = (c2 - c1 + 1) * (r2 - r1 + 1)
d = 1
x, y = 0, 0
dist = 1
num = 1
max_num = 0
while total > 0:
    for _ in range(2):
        for _ in range(dist):
            if r1 <= x <= r2 and c1 <= y <= c2:
                grid[x - r1][y - c1] = num
                total -= 1
                max_num = num
            dx, dy = dirs[d]
            x += dx
            y += dy
            num += 1
        d = (d - 1) % 4
    dist += 1
max_len = len(str(max_num))
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(grid[i][j]).rjust(max_len), end=' ')
    print()
